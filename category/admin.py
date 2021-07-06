from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    search_fields = ('name', )
    list_filter = ('name', )
    prepopulated_fields = {'slug': ('name',)}
