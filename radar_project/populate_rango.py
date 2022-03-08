import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from radar.models import FriendList, Session, UserProfile

def populate():
    user_profile = [
        {'id': 'charles123', 'firstName': 'charles',
         'lastName': 'dickinson',
         'age': 17, 'shareLocation': True } ]

    # friend_list = []

    # sessions_in_area = { }

def add_userProfile(userId, firstName, lastName, age, shareLocation):
    user = UserProfile.objects.get_or_create(userId = userId,
                                             firstName = firstName,
                                             lastName = lastName, age=age)
    user.shareLocation = shareLocation
    user.save()
    return user

def add_friend(userId, firstName, lastName, age, shareLocation=True):
    friend = FriendList.objects.get_or_create(userId = userId
