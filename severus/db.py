import os

from peewee import (
    CharField, DateTimeField, ForeignKeyField, IntegerField, Model as _Model)
from playhouse.db_url import connect


db = connect(os.getenv('DATABASE_URL'))


class Model(_Model):
    class Meta:
        database = db


class User(Model):
    adress = CharField()
    name = CharField()


class Task(Model):
    user = ForeignKeyField(User, related_name='tasks')
    title = CharField()
    due_date = DateTimeField()
    STATUS_CHOICES = (
        (0, 'open'),
        (1, 'hidden'),
        (2, 'assigned'),
        (3, 'completed')
    )
    status = IntegerField(choices=STATUS_CHOICES)
    description = CharField(null=True)
    estimated_time_in_minutes = IntegerField(null=True)


class StandardTask(Model):
    title = CharField()
    name = CharField()
