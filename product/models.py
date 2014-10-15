from django.db import models
from client.models import ClientCalendar

class FoodCalendar(models.Model):
    food_time_choices = (
        (1, 'breakfast'),
        (2, 'lunch'),
        (3, 'dinner'),
        (4, 'supper'),
    )
    calendar_id = models.ForeignKey(ClientCalendar)
    food_id = models.ForeignKey(Food)
    weight = models.DecimalField()
    food_time = models.IntegerField(choices=food_time_choices)

class Food(models.Model):
    name = models.CharField(max_length=200)
    preparing_method = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=200)
    kkal = models.DecimalField()
    b = models.DecimalField()
    j = models.DecimalField()
    u = models.DecimalField()

class FoodToProduct(models.Model):
    food_id = models.ForeignKey(Food)
    product_id = models.ForeignKey(Product)
    product_weight = models.IntegerField()