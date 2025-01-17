# Generated by Django 4.1.6 on 2023-02-06 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=1, max_length=255, verbose_name='Nomi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Holati'),
        ),
    ]
