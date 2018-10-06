from flask import Flask
from flask_cors import CORS
from flask_potion import Api, fields, ModelResource
from flask_potion.contrib.peewee import PeeweeManager

from severus.db import Bid, User, Task, Category
from severus.utils import get_version


app = Flask('severus')
CORS(app)
api = Api(app, default_manager=PeeweeManager)


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


class CategoryResource(ModelResource):
    class Meta:
        model = Category
        name = 'categories'


class TaskResource(ModelResource):
    class Meta:
        model = Task
        name = 'tasks'

    class Schema:
        due_date = fields.DateString()
        category = ToOneInteger(CategoryResource)
        user = ToOneInteger(UserResource)
        bids = ToManyInteger('bids')


class BidResource(ModelResource):
    class Meta:
        model = Bid
        name = 'bids'

    class Schema:
        user = ToOneInteger(UserResource)
        task = ToOneInteger(TaskResource)


api.add_resource(UserResource)
api.add_resource(TaskResource)
api.add_resource(BidResource)
api.add_resource(CategoryResource)
