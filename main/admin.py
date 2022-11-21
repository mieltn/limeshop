from django.contrib import admin
from .models import Category, Cuisine, Recipe, Ingredient, Basket


admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Basket)
