from tabnanny import verbose
from django.db import models

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django_mysql.models import ListCharField

# Create your models here.


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    age = models.IntegerField(default=18)
    slug = models.SlugField(unique=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=5000)
    views = models.IntegerField(default=0)
    # many to many because we want to register what user is liking!
    likes = models.ManyToManyField(User, related_name="posts")
    image = models.ImageField(upload_to='images/', blank=True)
    review = models.IntegerField(default=5)
    comments = ListCharField(
        base_field=models.CharField(max_length=5000),
        max_length=(5000),
        blank=True
    )
    slug = models.SlugField(unique=True)

    total_likes = models.IntegerField(default=0)

    # allows us to count number of likes
    def set_total_likes(self):
        self.total_likes = self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title
