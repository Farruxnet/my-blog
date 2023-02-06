from django.shortcuts import render

from apps.app.utils.site_context import context_site_sum
from apps.blog.models import Post


def post_detail(request, slug=None):
    try:
        post_obj = Post.objects.select_related('created_by', 'updated_by').get(slug=slug)
        context = context_site_sum({
            'post': post_obj,
            'page_title': post_obj.name
        })
        return render(request, "post.html", context=context)
    except Post.DoesNotExist:
        return render(request, "404.html")
