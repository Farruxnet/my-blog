from django.db import models

from apps.app.models import BaseModel
from apps.users.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class Category(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("Nomi"))
    slug = models.SlugField(blank=True, verbose_name=_("Slug"))
    sub_category = models.ManyToManyField("self", blank=True, verbose_name=_("Bo'lim"))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Bo'lim")
        verbose_name_plural = _("Bo'limlar")


class Tag(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("Nomi"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Taglar")


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Avtor"))
    name = models.CharField(max_length=255, verbose_name=_("Nomi"))
    text = CKEditor5Field(verbose_name=_("To'liq matn"))
    category = models.ManyToManyField(Category, verbose_name=_("Bo'lim"))
    tag = models.ManyToManyField(Tag, verbose_name=_("Taglar"))
    photo = models.ImageField(upload_to='post_images/', verbose_name=_("Post uchun rasm"))
    views = models.IntegerField(default=0, verbose_name=_("Ko'rishlar soni"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Postlar")


class Comments(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Avtor"))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_("Post"))
    text = CKEditor5Field(max_length=1024, verbose_name=_("Izoh matni"))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("Izoh")
        verbose_name_plural = _("Izohlar")
