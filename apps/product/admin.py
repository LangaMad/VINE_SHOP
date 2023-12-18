from django.contrib import admin
from django.contrib import admin
from .models import Product , Category
# Register your models here.
from django.utils.html import format_html
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_products =[
        'name',
        'price',
        'description',
        'brand',
        'photo',
        'public_date',
        'count'
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'photo',
        'product',
    ]

