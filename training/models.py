from django.db import models
from client.models import ClientCalendar


class Muscle(models.Model):
    name = models.CharField(max_length=200)


class Training(models.Model):
    type_choices = (
        (1,'',),
        (2,'',),
        (3,'',),
        (4,'',),
    )
    equipment_choices = (
        (1,'',),
        (2,'',),
        (3,'',),
        (4,'',),
    )
    difficulty_choices = (
        (1,'',),
        (2,'',),
        (3,'',),
        (4,'',),
    )
    name = models.CharField(max_length=200)
    tr_type = models.IntegerField(choices=type_choices)
    equipment = models.IntegerField(choices=equipment_choices)
    difficulty = models.IntegerField(choices=difficulty_choices)
    description = models.TextField()

class TrainingToMuscle(models.Model):
    muscle = models.ForeignKey(Muscle)
    training = models.ForeignKey(Training)
    is_primary = models.IntegerField()


class TrainingCalendar(models.Model):
    calendar_id = models.ForeignKey(ClientCalendar)
    training_id = models.ForeignKey(Training)