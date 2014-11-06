from django.db import models
from client.models import ClientCalendar


class Food(models.Model):
    name = models.CharField(max_length=200)
    preparing_method = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Блюда'


class FoodCalendar(models.Model):
    food_time_choices = (
        (1, 'breakfast'),
        (2, 'lunch'),
        (3, 'dinner'),
        (4, 'supper'),
    )
    calendar_id = models.ForeignKey(ClientCalendar)
    food_id = models.ForeignKey(Food)
    weight = models.FloatField()
    food_time = models.IntegerField(choices=food_time_choices)


class Product(models.Model):
    name = models.CharField(max_length=200)
    kkal = models.FloatField()
    b = models.FloatField()
    j = models.FloatField()
    u = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Продукты'

class FoodToProduct(models.Model):
    food_id = models.ForeignKey(Food)
    product_id = models.ForeignKey(Product)
    product_weight = models.IntegerField()