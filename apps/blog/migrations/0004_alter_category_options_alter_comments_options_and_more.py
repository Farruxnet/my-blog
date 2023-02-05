# Generated by Django 4.1.6 on 2023-02-05 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_remove_comments_create_at_remove_post_create_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': "Bo'lim", 'verbose_name_plural': "Bo'limlar"},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Izoh', 'verbose_name_plural': 'Izohlar'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Postlar'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Taglar'},
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqi"),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_%(model_name)ss', to=settings.AUTH_USER_MODEL, verbose_name="Qo'shdi"),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='sub_category',
            field=models.ManyToManyField(blank=True, to='blog.category', verbose_name="Bo'lim"),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_%(model_name)ss', to=settings.AUTH_USER_MODEL, verbose_name='Yangiladi'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqi"),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_%(model_name)ss', to=settings.AUTH_USER_MODEL, verbose_name="Qo'shdi"),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(max_length=1024, verbose_name='Izoh matni'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_%(model_name)ss', to=settings.AUTH_USER_MODEL, verbose_name='Yangiladi'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Avtor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blog.category', verbose_name="Bo'lim"),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqi"),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_%(model_name)ss', to=settings.AUTH_USER_MODEL, verbose_name="Qo'shdi"),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='post_images/', verbose_name='Post uchun rasm'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.tag', verbose_name='Taglar'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="To'liq matn"),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_%(model_name)ss', to=settings.AUTH_USER_MODEL, verbose_name='Yangiladi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Avtor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0, verbose_name="Ko'rishlar soni"),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqi"),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_%(model_name)ss', to=settings.AUTH_USER_MODEL, verbose_name="Qo'shdi"),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_%(model_name)ss', to=settings.AUTH_USER_MODEL, verbose_name='Yangiladi'),
        ),
    ]