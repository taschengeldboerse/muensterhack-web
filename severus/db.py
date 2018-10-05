import datetime
import os

from peewee import (
    CharField, DateTimeField, ForeignKeyField, IntegerField, Model as _Model)
from playhouse.db_url import connect


db = connect(os.getenv('DATABASE_URL'))


class Model(_Model):
    class Meta:
        database = db


class User(Model):
    address = CharField()
    name = CharField()


class Task(Model):
    user = ForeignKeyField(User, related_name='tasks')
    title = CharField()
    description = CharField(null=True)
    due_date = DateTimeField()
    STATUS_CHOICES = (
        (0, 'open'),
        (1, 'hidden'),
        (2, 'assigned'),
        (3, 'completed')
    )
    status = IntegerField(choices=STATUS_CHOICES)
    estimated_time_in_minutes = IntegerField(null=True)
    assignee = ForeignKeyField(User, related_name='assigned_tasks', null=True)


class StandardTask(Model):
    title = CharField()
    description = CharField()


class Bid(Model):
    user = ForeignKeyField(User, related_name='bids')
    task = ForeignKeyField(Task, related_name='bids')
    timestamp = DateTimeField(default=datetime.datetime.utcnow)
