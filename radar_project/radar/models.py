from django.db import models

# Create your models here.

class FriendList(models.Model):
    
    userId_fk = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    friendId_fk = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.friendId_fk

class Session(models.Model):
    
    private = models.BooleanField(default=True)
    hasArrived = models.BooleanField(default = False)
    destination = models.CharField(max_length=128, unique=True)
    userId_fk = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.destination
