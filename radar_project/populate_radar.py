import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'radar_project.settings')

import django
django.setup()
from radar.models import FriendList, Session, UserProfile
from django.contrib.auth.models import User

def populate():
    user_profile = [
        {'id': 'charles123', 'name': 'charles dickinson',
         'age': 17, 'shareLocation': False } ]

    # friend_list = []
    # sessions_in_area = { }

    for user_dict in user_profile:
        add_userProfile(user_dict)
        print(f'- {user_dict["name"]}')

def add_userProfile(user_dict):
    u = UserProfile.objects.get_or_create(
        user.username = user_dict['name'],
        age = user_dict['age'], shareLocation = user_dict['shareLocation'])[0]
    u.save()
    return u

if __name__ == '__main__':
    print('Starting Radar population script...')
    populate()
