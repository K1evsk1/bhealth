from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    calories = models.FloatField(verbose_name='Калории')
    protein = models.FloatField(verbose_name='Белки')
    fat = models.FloatField(verbose_name='Жиры')
    carbs = models.FloatField(verbose_name='Углеводы')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Продукты'


class Dish(models.Model):
    product = models.ManyToManyField(Product, through='DishToProduct')
    dish_name = models.CharField(max_length=100, verbose_name='Наименование блюда')

    def __str__(self):
        return self.dish_name

    class Meta:
        verbose_name_plural = 'Блюда'


class DishToProduct(models.Model):
    dish = models.ForeignKey(Dish, verbose_name='Блюдо')
    product = models.ForeignKey(Product, verbose_name='Продукт')
    weight = models.IntegerField(verbose_name='Вес продукта в блюде')

    def __str__(self):
        return self.dish.dish_name
