from flask import Flask
from flask_potion import Api, ModelResource
from flask_potion.contrib.peewee import PeeweeManager

from severus.db import User, Task
from severus.utils import get_version


app = Flask('severus')


api = Api(app, default_manager=PeeweeManager)


@app.route('/')
def root():
    return get_version()


class UserResource(ModelResource):
    class Meta:
        model = User


class TaskResource(ModelResource):
    class Meta:
        model = Task


api.add_resource(UserResource)
api.add_resource(TaskResource)
