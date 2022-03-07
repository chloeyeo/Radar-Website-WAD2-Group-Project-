from django.contrib import admin
from radar.models import UserProfile, FriendList, Session

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(FriendList)
admin.site.register(Session)
