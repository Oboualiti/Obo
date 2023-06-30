from django.contrib import admin
from .models import Products,Customer_info,Email,Customer_infobycart
# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name","clasement"]
@admin.register(Customer_info)
class Customer_infoAdmin(admin.ModelAdmin):
    list_display = ['full_name','city']
admin.site.register(Email)

admin.site.register(Customer_infobycart)
