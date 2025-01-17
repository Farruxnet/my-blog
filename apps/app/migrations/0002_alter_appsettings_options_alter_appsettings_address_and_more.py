# Generated by Django 4.1.6 on 2023-02-05 08:25

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appsettings',
            options={'verbose_name': 'Sayt sozlamasi', 'verbose_name_plural': 'Sayt sozlamalri'},
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='address',
            field=models.TextField(max_length=255, verbose_name='Manzil'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='email',
            field=models.EmailField(max_length=128, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='facebook',
            field=models.CharField(max_length=64, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='footer',
            field=django_ckeditor_5.fields.CKEditor5Field(max_length=1024, verbose_name='Sayt pastgi qismi'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='github',
            field=models.CharField(max_length=64, verbose_name='Github'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='gitlab',
            field=models.CharField(max_length=64, verbose_name='Gitlab'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='header',
            field=django_ckeditor_5.fields.CKEditor5Field(max_length=1024, verbose_name='Sayt tepa qismi'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='instagram',
            field=models.CharField(max_length=64, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='linkedin',
            field=models.CharField(max_length=64, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='Telefon raqam'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='telegram',
            field=models.CharField(max_length=64, verbose_name='Telegram'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='title',
            field=models.TextField(max_length=255, verbose_name='Sayt sarlavhasi'),
        ),
    ]
