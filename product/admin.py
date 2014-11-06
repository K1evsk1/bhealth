from django.contrib import admin
from product.models import Food, Product, FoodToProduct


admin.site.register(Food)
admin.site.register(Product)
admin.site.register(FoodToProduct)