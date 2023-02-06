from django.shortcuts import render

from app.utils.site_context import context_site_sum


def home(request):
    context = context_site_sum({
        'page_title': "Bosh sahifa"
    })
    return render(request, "home.html", context=context)
