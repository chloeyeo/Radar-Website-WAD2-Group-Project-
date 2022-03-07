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
