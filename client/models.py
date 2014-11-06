from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    gender_choices = (
        (1, 'Мужчина'),
        (2, 'Женщина'),
    )
    activity_choice = (
        (1, 'Пассивный'),
        (2, 'Легкий'),
        (3, 'Активный'),
        (4, 'Очень активный'),
    )
    goal_choice = (
        (1, 'Похудеть'),
        (2, 'Остаться в форме'),
        (3, 'Набрать вес'),
    )
    coach_choices = (
        (1, 'Есть'),
        (2, 'Нет'),
    )
    user = models.OneToOneField(User, related_name='client')
    unique_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True)
    gender = models.IntegerField(choices=gender_choices, blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    activity = models.IntegerField(choices=activity_choice, blank=True, null=True)
    count_training_to_week = models.IntegerField(blank=True, null=True)
    count_minute_to_training = models.IntegerField(blank=True, null=True)
    goal = models.IntegerField(choices=goal_choice, blank=True, null=True)
    have_a_coach = models.IntegerField(choices=coach_choices, blank=True)
    avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.email or self.unique_id


class ClientCalendar(models.Model):
    client_id = models.ForeignKey(Client)
    date = models.DateField()