from django.shortcuts import render

from apps.app.utils.site_context import context_site_sum
from apps.app.models import Page


def page(request, slug=None):
    try:
        page_obj = Page.objects.select_related('created_by', 'updated_by').get(slug=slug)
        context = context_site_sum({
            'page': page_obj,
            'page_title': page_obj.title
        })
        return render(request, "page.html", context=context)
    except Page.DoesNotExist:
        return render(request, "404.html")
