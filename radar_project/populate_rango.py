import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from radar.models import FriendList, Session, UserProfile

def populate():

    userprof = UserProfile()

    user_profile = [
        {'id': userprof.user, 'firstName': userprof.firstName,
         'lastName': userprof.lastName
         'age': userProf.age, 'shareLocation': userProf.shareLocation} ]

    friend_list = [ 

    sessions_in_area = {

def add_userProfile(userId, firstName, lastName, age, shareLocation):
    user = UserProfile.objects.get_or_create(userId = userId,
                                             firstName = firstName,
                                             lastName = lastName, age=age)
    user.shareLocation = shareLocation
    user.save()
    return user

def add_friend(userId, firstName, lastName, age, shareLocation=True):
    friend = FriendList.objects.get_or_create(userId = userId
