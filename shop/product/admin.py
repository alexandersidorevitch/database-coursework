from django.contrib import admin

# Register your models here.
from .models import Address, Category, Customer, Order, Product, Shop

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Customer)
