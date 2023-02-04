from django.urls import path

from apps.blog.views.blog import blog
from apps.blog.views.post_detail import post_detail

urlpatterns = [
    path('post', post_detail, name='post-detail'),
    path('', blog, name='blog')
]
