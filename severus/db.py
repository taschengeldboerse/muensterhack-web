import datetime
import os

from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.types.choice import ChoiceType


app = Flask('severus')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SEVERUS_SECRET_KEY', 'debug_key')
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String)
    email = db.Column(db.String)
    sex = db.Column(db.String)
    birthday = db.Column(db.Date)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Task(db.Model):
    __tablename__ = 'tasks'

    STATUS_CHOICES = (
        (0, 'open'),
        (1, 'hidden'),
        (2, 'assigned'),
        (3, 'completed')
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship(
        User, backref=db.backref('tasks', lazy=True), foreign_keys=[user_id])
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    due_date = db.Column(db.Date, nullable=False)
    status = db.Column(ChoiceType(STATUS_CHOICES), nullable=False)
    estimated_time_in_minutes = db.Column(db.Integer)
    assignee_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    assignee = db.relationship(
        User,
        backref=db.backref('assigned_tasks', lazy=True),
        foreign_keys=[assignee_id])
    category_id = db.Column(
        db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship(
        Category, backref=db.backref('tasks', lazy=True))


class TaskTemplate(db.Model):
    __tablename__ = 'task_templates'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)


class Bid(db.Model):
    __tablename__ = 'bids'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship(User, backref=db.backref('bids', lazy=True))
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    task = db.relationship(Task, backref=db.backref('bids', lazy=True))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
