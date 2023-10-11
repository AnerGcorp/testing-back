from django.contrib import admin

# Register your models here.
from .models import Menu, MenuCategory


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):

    fields = ['name', 'verbose_name', ]
    list_display = ['__str__', ]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    fields = ['name', 'category', 'path', 'parent', ]
    list_display = ['__str__', 'category', 'path', 'parent', ]