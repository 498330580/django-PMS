from django.contrib import admin

# Register your models here.

from .models import Menu, WebsiteConfig


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_type', 'desc')


class WebsiteConfigAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(WebsiteConfig, WebsiteConfigAdmin)
