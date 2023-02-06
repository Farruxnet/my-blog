from apps.app.models import AppSettings
from collections import Counter


def context_site_sum(obj):
    context_site = AppSettings.objects.last()
    context = {
        'title': context_site.title,
        'footer': context_site.footer,
        'facebook': context_site.facebook,
        'instagram': context_site.instagram,
        'telegram': context_site.telegram,
        'linkedin': context_site.linkedin,
        'github': context_site.github,
        'gitlab': context_site.gitlab,
        'email': context_site.email,
        'phone_number': context_site.phone_number,
        'address': context_site.address,
    }
    context.update(obj)
    return context
