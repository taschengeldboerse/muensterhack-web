from flask import Flask
from flask_cors import CORS
from flask_potion import Api, fields, ModelResource
from flask_potion.contrib.peewee import PeeweeManager

from severus.db import User, Task
from severus.utils import get_version


app = Flask('severus')
CORS(app)
api = Api(app, default_manager=PeeweeManager)


@app.route('/')
def root():
    return get_version()


class UserResource(ModelResource):
    class Meta:
        model = User
        name = 'users'


class TaskResource(ModelResource):
    class Meta:
        model = Task
        name = 'tasks'

    class Schema:
        due_date = fields.DateString()
        user = fields.ToOne(UserResource)


api.add_resource(UserResource)
api.add_resource(TaskResource)
