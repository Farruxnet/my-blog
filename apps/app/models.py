from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, related_name='created_by_%(model_name)ss')
    updated_by = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, related_name='updated_by_%(model_name)ss')

    class Meta:
        abstract = True


class AppSettings(models.Model):
    title = models.TextField(max_length=255)
    footer = CKEditor5Field(max_length=1024)
    header = CKEditor5Field(max_length=1024)
    facebook = models.CharField(max_length=64)
    instagram = models.CharField(max_length=64)
    telegram = models.CharField(max_length=64)
    linkedin = models.CharField(max_length=64)
    github = models.CharField(max_length=64)
    gitlab = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)
    phone_number = models.CharField(max_length=12)
    address = models.TextField(max_length=255)

    def __str__(self):
        return "Sayt sozlamalari"
