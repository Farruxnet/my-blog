from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Qo'shilgan vaqi"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, related_name='created_by_%(model_name)ss', verbose_name=_("Qo'shdi"))
    updated_by = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, related_name='updated_by_%(model_name)ss', verbose_name=_("Yangiladi"))

    class Meta:
        abstract = True


class AppSettings(models.Model):
    title = models.TextField(max_length=255, verbose_name=_("Sayt sarlavhasi"))
    footer = CKEditor5Field(max_length=1024, verbose_name=_("Sayt pastgi qismi"))
    header = CKEditor5Field(max_length=1024, verbose_name=_("Sayt tepa qismi"))
    facebook = models.CharField(max_length=64, verbose_name=_("Facebook"))
    instagram = models.CharField(max_length=64, verbose_name=_("Instagram"))
    telegram = models.CharField(max_length=64, verbose_name=_("Telegram"))
    linkedin = models.CharField(max_length=64, verbose_name=_("Linkedin"))
    github = models.CharField(max_length=64, verbose_name=_("Github"))
    gitlab = models.CharField(max_length=64, verbose_name=_("Gitlab"))
    email = models.EmailField(max_length=128, verbose_name=_("Email"))
    phone_number = models.CharField(max_length=12, verbose_name=_("Telefon raqam"))
    address = models.TextField(max_length=255, verbose_name=_("Manzil"))

    def __str__(self):
        return _("Sayt sozlamalri")

    class Meta:
        verbose_name = _("Sayt sozlamasi")
        verbose_name_plural = _("Sayt sozlamalri")