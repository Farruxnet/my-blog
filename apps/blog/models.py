from django.db import models
from apps.users.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    text = models.TextField()
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)
    photo = models.ImageField(upload_to = 'post_images/')
    create_at = models.DateTimeField(default = timezone.now)
    views = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    text = models.CharField(max_length = 512)
    create_at = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.text

















#
