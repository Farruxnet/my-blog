from django.shortcuts import render

from app.utils.site_context import context_site
from apps.app.models import Page


def page(request, slug=None):
    try:
        page_obj = Page.objects.select_related('created_by', 'updated_by').get(slug=slug)
        context = {
            'page': page_obj,
            'context_site': context_site()
        }
        return render(request, "page.html", context=context)
    except Page.DoesNotExist:
        return render(request, "404.html")
