from flask_cors import CORS
from flask_login import current_user, LoginManager
from flask_potion import Api, fields, ModelResource
from flask_potion.contrib.alchemy import SQLAlchemyManager
from flask_potion.contrib.principals import principals
from flask_principal import (
    Principal, Identity, UserNeed, AnonymousIdentity, identity_loaded,
    RoleNeed)

from severus.db import app, Bid, User, Task, Category
from severus.utils import get_version


CORS(app)


principal = Principal(app)
login_manager = LoginManager(app)

api = Api(
    app,
    # default_manager=principals(SQLAlchemyManager),
    # decorators=[login_required],
)


@login_manager.request_loader
def get_user(request):
    if request.authorization:
        # TODO: replace with actual password check
        username, password = (
            request.authorization.username, request.authorization.password)
        if username == password:
            return User.get(User.name == username)
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


class ToOneInteger(fields.ToOne):

    def format(self, value):
        return value.id


class ToManyInteger(fields.ToMany):

    def format(self, value):
        return [x.id for x in value]


class UserResource(ModelResource):
    class Meta:
        model = User
        name = 'users'
        permissions = {
            'update': 'admin',
        }


class CategoryResource(ModelResource):
    class Meta:
        model = Category
        name = 'categories'
        permissions = {
            'create': 'admin',
        }


class TaskResource(ModelResource):
    class Meta:
        model = Task
        name = 'tasks'
        permissions = {
            'create': 'admin',
        }

    class Schema:
        due_date = fields.DateString()
        category = ToOneInteger(CategoryResource)
        user = ToOneInteger(UserResource)
        bids = ToManyInteger('bids')


class BidResource(ModelResource):
    class Meta:
        model = Bid
        name = 'bids'
        permissions = {
            'create': 'anybody',
            'update': ['user:user', 'admin'],
        }

    class Schema:
        user = ToOneInteger(UserResource)
        task = ToOneInteger(TaskResource)
        timestamp = fields.DateTimeString(nullable=True)


api.add_resource(UserResource)
api.add_resource(TaskResource)
api.add_resource(BidResource)
api.add_resource(CategoryResource)
