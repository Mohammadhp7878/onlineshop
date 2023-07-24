from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent']
    ordering = ['parent', 'name']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'inventory', 'price']
    ordering = ['name', 'price']
    search_fields = ['name', 'category']

@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'logo']