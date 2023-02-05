from apps.app.models import AppSettings


def context_site():
    context = AppSettings.objects.last()
    return context
