from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField


class User():
    adress = CharField()
    name = CharField()


class Task():
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


class StandardTasks():
    title = CharField()
    name = CharField()
