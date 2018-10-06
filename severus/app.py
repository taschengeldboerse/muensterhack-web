from flask import request
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity
from flask_login import current_user, login_required, LoginManager
from flask_potion import Api, fields, ModelResource
from flask_potion.contrib.alchemy import SQLAlchemyManager
from flask_potion.contrib.principals import principals
from flask_principal import (
    Principal, Identity, UserNeed, AnonymousIdentity, identity_loaded,
    RoleNeed)

from severus.db import app, Bid, User, Task, Category
from severus.utils import DEFAULT_LATLON, get_distance, get_latlon, get_version


CORS(app)


principal = Principal(app)
login_manager = LoginManager(app)

api = Api(
    app,
    # default_manager=principals(SQLAlchemyManager),
    # decorators=[login_required],
)


def authenticate(username, password):
    # TODO: Replace with real password check
    if username == password:
        return User.query.filter_by(name=username).first()


def identity(payload):
    return User.query.filter_by(id=payload['user_id']).first()


jwt = JWT(app, authenticate, identity)


@login_manager.request_loader
def get_user(request):
    if request.authorization:
        # TODO: Check JWT
        username, password = (
            request.authorization.username, request.authorization.password)
        if username == password:
            return User.query.filter_by(name=username).first()
    return None


@principal.identity_loader
def get_identity():
    if current_user.is_authenticated:
        return Identity(current_user.id)
    return AnonymousIdentity()


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    if not isinstance(identity, AnonymousIdentity):
        identity.provides.add(UserNeed(identity.id))
        if current_user.is_admin:
            identity.provides.add(RoleNeed('admin'))


@app.route('/')
def root():
    return get_version()


class ToOneIntegerField(fields.ToOne):

    def format(self, value):
        return value.id


class ToManyIntegerField(fields.ToMany):

    def format(self, value):
        return [x.id for x in value]


class DistanceField(fields.PositiveInteger):

    def _get_arg(self, arg, default=None):
        return request.args.get(
            arg,
            request.headers.get(arg, default))

    def format(self, value):
        # XXX: Hotfix for old seeding data encoding issues
        value = value.replace('Ã¼', 'ü')
        value = value.replace('Ã', 'ß')
        task_lat_lon = get_latlon(value)
        # TODO: Use user address to determine default latlon
        user_lat_lon = (
            self._get_arg('lat', default=DEFAULT_LATLON[0]),
            self._get_arg('lon', default=DEFAULT_LATLON[1]),
        )
        return super().format(get_distance(task_lat_lon, user_lat_lon))


class UserResource(ModelResource):
    class Meta:
        model = User
        name = 'users'
        permissions = {
            'update': 'admin',
        }

    class Schema:
        id = fields.Integer(io='r')
        bids = ToManyIntegerField('bids')


class CategoryResource(ModelResource):
    class Meta:
        model = Category
        name = 'categories'
        permissions = {
            'create': 'admin',
        }

    class Schema:
        id = fields.Integer(io='r')


class TaskResource(ModelResource):
    class Meta:
        model = Task
        name = 'tasks'
        permissions = {
            'create': 'admin',
        }

    class Schema:
        id = fields.Integer(io='r')
        due_date = fields.DateString()
        category = ToOneIntegerField(CategoryResource)
        user = ToOneIntegerField(UserResource)
        bids = ToManyIntegerField('bids')
        distance_in_meters = DistanceField(io='r', attribute='location')


class BidResource(ModelResource):
    class Meta:
        model = Bid
        name = 'bids'
        permissions = {
            'create': 'anybody',
            'update': ['user:user', 'admin'],
        }

    class Schema:
        id = fields.Integer(io='r')
        user = ToOneIntegerField(UserResource)
        task = ToOneIntegerField(TaskResource)
        timestamp = fields.DateTimeString(io='r')


api.add_resource(UserResource)
api.add_resource(TaskResource)
api.add_resource(BidResource)
api.add_resource(CategoryResource)
