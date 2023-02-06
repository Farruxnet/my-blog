from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render

from apps.app.utils.site_context import context_site_sum
from apps.blog.models import Post


def blog(request):
    paginator = Paginator(Post.objects.filter(is_active=True).order_by('-id'), settings.PAGE_SIZE)
    page_number = request.GET.get('page') if 'page' in request.GET else 1
    page_obj = paginator.get_page(page_number)
    context = context_site_sum({
        'posts': page_obj,
        'page_title': "Blog",
    })
    return render(request, "blog.html", context=context)
