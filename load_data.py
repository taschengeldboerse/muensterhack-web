import datetime as dt
import csv
import io

from severus.db import db, User, Task, TaskTemplate, Category

session = db.session

def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        instance = model(**kwargs)
        session.add(instance)
        return instance, True

# Users
input_file = csv.DictReader(
    io.open("data_examples/user_examples.csv", encoding='utf-8'),
    delimiter=';'
)
user_list = []
for counter, row in enumerate(input_file):
    user_example = dict(row)
    user_list.append(User(
        name=user_example['name'], address=user_example['address']))
    get_or_create(
        session, User, name=user_example['name'],
        address=user_example['address']
    )

session.commit()

# Category
input_file = csv.DictReader(
    io.open("data_examples/category_examples.csv", encoding='utf-8'),
    delimiter=';'
)
category_list = []
for counter, row in enumerate(input_file):
    category_example = dict(row)
    category_list.append(Category(name=category_example['Kategorie']))
    get_or_create(
        session, Category, name=category_example['Kategorie']
    )

session.commit()

# Task
old_to_new_cat = {
    1: 6,
    2: 3,
    3: 1,
    4: 4,
    5: 7,
    6: 5,
    7: 2
}

input_file = csv.DictReader(
    io.open("data_examples/task_examples.csv", encoding='utf-8'),
    delimiter=';'
)
task_list = []
for line in input_file:
    temp = dict(line)
    task_example = {
        'user_id': int(temp['user']),
        'title': temp['Title'],
        'due_date': dt.datetime.strptime(temp['due_date'], "%d.%m.%Y"),
        'status': 0,
        'description': temp['description'][:255],
        'estimated_time_in_minutes': int(temp['estimated_time_in_minutes']),
        'assignee': None,
        'category_id': old_to_new_cat[int(temp['Category'])]
    }
    task_list.append(task_example)

session.execute(Task.__table__.insert() ,task_list)
session.commit()

# df_standtask = [
#     {'title': 'Rasenmähen', 'description': 'test'},
#     {'title': 'Einkaufen', 'description': 'test'}
# ]
