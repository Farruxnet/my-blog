from django.contrib import admin

from apps.app.models import AppSettings, Page


@admin.register(AppSettings)
class AppSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass
