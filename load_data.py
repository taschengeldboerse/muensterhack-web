import datetime as dt

from severus.db import User, Task, StandardTask

df_user = [
    {'name': 'Oma Müller', 'address': 'Hafenstraße 16, Münster 48153'},
    {'name': 'Opa Müller', 'address': 'Hafenstraße 16, Münster 48153'},
    {'name': 'Kind Tim', 'address': 'Hafenstraße 26, Münster 48153'}
]

oma = User.create(name='Oma Müller', address='Hafenstraße 16, Münster 48153')
opa = User.create(name='Opa Müller', address='Hafenstraße 16, Münster 48153')
kind = User.create(name='Kind Tim', address='Hafenstraße 16, Münster 48153')


df_task = [
    {
        'user': oma, 'title': 'Einkaufen', 'due_date': dt.datetime(2018, 10, 20),
        'status': 0, 'description': '- Brot\n- 5 Äpfel',
        'estimated_time_in_minutes': 20, 'assignee': None
    },
    {
        'user': oma, 'title': 'Staubsaugen', 'due_date': dt.datetime(2018, 10, 10),
        'status': 3, 'description': 'Es wäre nett, wenn jemand meine 4 Zimmerwohnung staubsaugen könnte.',
        'estimated_time_in_minutes': 30, 'assignee': kind
    },
    {
        'user': opa, 'title': 'Rasenmähen', 'due_date': dt.datetime(2018, 10, 20),
        'status': 2, 'description': None,
        'estimated_time_in_minutes': 30, 'assignee': kind
    }

]

df_standtask = [
    {'title': 'Rasenmähen', 'description': 'test'},
    {'title': 'Einkaufen', 'description': 'test'}
]

Task.insert_many(df_task).execute()
StandardTask.insert_many(df_standtask).execute()