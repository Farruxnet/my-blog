# Generated by Django 4.1.6 on 2023-02-06 14:11

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appsettings',
            name='facebook',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='footer',
            field=models.TextField(max_length=255, verbose_name='Sayt pastgi qismi'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='github',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Github'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='gitlab',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Gitlab'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='header',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, max_length=1024, null=True, verbose_name='Sayt tepa qismi'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='instagram',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='linkedin',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='telegram',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Telegram'),
        ),
    ]