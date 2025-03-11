from django.contrib import admin

from core.models import Order, Product, Rating, Restaurant, Sale

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Sale)
admin.site.register(Rating)
admin.site.register(Product)
admin.site.register(Order)
