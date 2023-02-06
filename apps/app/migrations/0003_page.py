# Generated by Django 4.1.6 on 2023-02-05 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_appsettings_options_alter_appsettings_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqi")),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')),
                ('title', models.CharField(max_length=255)),
                ('body', django_ckeditor_5.fields.CKEditor5Field()),
                ('views', models.PositiveIntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_%(model_name)ss', to=settings.AUTH_USER_MODEL, verbose_name="Qo'shdi")),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_%(model_name)ss', to=settings.AUTH_USER_MODEL, verbose_name='Yangiladi')),
            ],
            options={
                'verbose_name': 'Sahifa',
                'verbose_name_plural': 'Sahifalar',
            },
        ),
    ]