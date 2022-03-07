from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    host = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    shareLocation = models.BooleanField(default=False)
    request = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class FriendList(models.Model):
    userId_fk = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.friendId_fk


class Session(models.Model):
    private = models.BooleanField(default=True)
    hasArrived = models.BooleanField(default=False)
    destination = models.CharField(max_length=128, unique=True)
    userId_fk = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE,)

    def __str__(self):
        return self.destination
