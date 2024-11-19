from django.contrib import admin
from .resource import CategoryResource
from .models import Category
from django import forms
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CategoryAdmin(ImportExportModelAdmin):
    category_class = CategoryResource

admin.site.register(Category, CategoryAdmin)

