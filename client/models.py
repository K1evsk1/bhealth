from django.db import models

class Client(models.Model):
    gender_choices = (
        (1, 'men'),
        (2, 'women'),
    )
    activity_choices = (
        (1, 'Sedentary: Spend most of the day sitting (e.g. bank teller, desk job) '),
        (2, 'Lightly Active: Spend a good part of the day on your feet (e.g. teacher, salesman) '),
        (3, 'Active: Spend a good part of the day doing some physical activity (e.g. waitress, mailman) '),
        (4, 'Very Active: Spend most of the day doing heavy physical activity (e.g. bike messenger, carpenter) '),
    )
    goal_choices = (
        (1, 'Lose Weight'),
        (2, 'Keep Fit'),
        (3, 'Gain Weight'),
    )
    nickname = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    gender = models.IntegerField(choices=gender_choices)
    date_of_birth = models.DateField()
    register_date = models.DateTimeField(auto_now_add=True)
    activity = models.IntegerField(choices=activity_choices)
    count_training_to_week = models.IntegerField()
    count_minute_to_training = models.IntegerField()
    goal = models.IntegerField(choices=goal_choices)

class ClientCalendar(models.Model):
    client_id = models.ForeignKey(Client)
    date = models.DateField()
