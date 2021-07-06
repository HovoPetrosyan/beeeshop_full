from django.contrib import admin
from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock', 'is_available',)
    list_filter = ('category', 'price',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
