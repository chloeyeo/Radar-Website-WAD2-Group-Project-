import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from radar.models import FriendList, Session, UserProfile

def populate():

    user_profile = [
        {'id': 'jane012', 'firstName': 'Jane', 'lastName': 'Wilkins',
         'age': 17, 'shareLocation': false } ]

    friend_list =

    sessions_in_area = 
