from django.contrib import admin

# Register your models here.

from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_type', 'desc')


admin.site.register(Menu, MenuAdmin)
