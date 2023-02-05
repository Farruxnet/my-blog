from django.contrib import admin

from apps.app.models import AppSettings, Page


@admin.register(AppSettings)
class AppSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AppSettings.objects.all():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['created_by', 'updated_by', 'views']
