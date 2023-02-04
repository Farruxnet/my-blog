from django.db import models

from apps.app.models import BaseModel
from apps.users.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.template.defaultfilters import slugify


class Category(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    sub_category = models.ManyToManyField("self", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = CKEditor5Field()
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)
    photo = models.ImageField(upload_to='post_images/')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comments(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = CKEditor5Field(max_length=1024)

    def __str__(self):
        return self.text

#
