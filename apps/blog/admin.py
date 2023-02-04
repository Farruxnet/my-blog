from django.contrib import admin

from apps.blog.models import Category, Tag, Post, Comments


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass
