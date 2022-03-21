import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'radar_project.settings')

import django
django.setup()
from radar.models import Category, Post
from django.contrib.auth.models import User

def populate():
    cartoon = [
        {'title' : 'Krusty krab', 'views': 12, 'likes':10, 'image' : "", 'description':'The Krusty Krab is a fictional fast food restaurant in the American animated television series SpongeBob SquarePants. It is famous for its signature burger, the Krabby Patty, the formula to which is a closely guarded trade secret.'},
        {'title' : 'Enchated Forest','views':24, 'likes':15, 'image': "", 'description':"Olaf. The Enchanted Forest is a location in Disney's 2019 animated feature film Frozen II. It is a dense, magical forest inhabited by the spirits of nature, and the Northuldra people."},
        {'title' : "Rupanzel's Tower",'views':17, 'likes':12, 'image': "", 'description' : "Rapunzel's Tower is a central location in Disney's 2010 animated feature film, Tangled. It is a secluded tower hidden deep within the woods outside of the kingdom Corona. Shortly after her birth, Princess Rapunzel was kidnapped by a woman named Mother Gothel, and locked away in the tower as an unknowing prisoner for eighteen years."},
        {'title' : "Gru's House" , 'views':46, 'likes':42, 'image': "", 'description' :"Gru's House is home of Felonius Gru, Lucy Wilde, Margo, Edith, Agnes, and also to the Minions, Dr. Nefario and Dru. Gru's lab is located right underneath. Unlike the neighboring track houses (homes that appear similar to others), it is made out of brick that is painted eerie black and a roof that is painted purple. It is also somewhat considerably larger. One similiarity it does share is that it is a two-story house."},
    ]

    anime = [
        {'title' : "Hawk's mum" ,'views':19, 'likes':14, 'image': "", 'description':'After rebuilding the Boar Hat, Hawk Mama is responsible for transporting the Seven Deadly Sins and Elizabeth to their next mission in Corand.'},
        {'title' : 'Avatar Temple' ,'views':23, 'likes':35, 'image': "", 'description' :"An Avatar Temple is a shrine built in honor of the Avatar. Each building bears a spiritual connection with the Avatar Spirit and all of its past incarnations, and as such is regarded as a sacrosanct dwelling. Some nations take this reverence for the Avatar Temple to an extreme, only permitting their respective religious authority to have regular access. For example, the Avatar Temple of the Air Nomads was open exclusively to the elder monks,[1] and only Fire Sages resided in the Fire Temple.[2] However, the Avatar is exempt from these restrictions."},
        {'title' : "Howl's Moving Castle" ,'views':18, 'likes':19, 'image': "",'description' : "The castle is actually Howl, it has different faces and lots of baggage which makes it heavy, it moves around to keep hidden, metaphors for a man who presents different faces to the world and keeps his true self hidden because of past hurt."},
        {'title' : 'Bathhouse' , 'views':72, 'likes':60, 'image': "", 'description' :"The Bathhouse, which stands on a half-dried swamp is a very grandiose and opulent structure on the island Yūya in the Spirit Realm. Built in a traditional Japanese bathhouse style, its color scheme encompasses shades of red, green and semi-dark tones of brown. A waterfall is also present at its bridge crossing."},
    ]

    movie = [
        {'title' : 'Horgwats' , 'views':54, 'likes':35, 'image': "",'description' : 'Hogwarts School of Witchcraft and Wizardry, often shortened to Hogwarts, was the British wizarding school, located in the Scottish Highlands.It accepted magical students from Great Britain and Ireland for enrolment.It was a state-owned school, funded by the Ministry of Magic.'},
        {'title' : 'Avengers Tower' , 'views':32, 'likes':25, 'image': "",'description':'Avengers Tower is a fictional location in the Marvel Cinematic Universe. It was the original headquarters of the Avengers.'},
        {'title' : 'Kamar-Taj' , 'views':37, 'likes':29, 'image': "",'description' : "Kamar-Taj - a mythical Tibetan city hidden in the Himalayan mountains where Doctor Strange receives his training as Sorcerer Supreme - is a rather textbook case of that second type, being a more-or-less direct lift of Shangri-La, the similarly mystical city at the center of James Hilton's classic novel Lost Horizon."},
        {'title' : 'Atlantis' , 'views':59, 'likes':50, 'image': "", 'description' :"Atlantis, a fabulously wealthy and advanced civilization, was swept into the sea and lost forever."},
    ]

    video_games = [
        {'title' : '1' , 'views':54, 'likes':35, 'image': "",'description' : 'game'},
        {'title' : '2' , 'views':32, 'likes':25, 'image': "",'description':'game'},
        {'title' : '3' , 'views':37, 'likes':29, 'image': "",'description' : "game"},
        {'title' : '4' , 'views':59, 'likes':50, 'image': "", 'description' :"game"},
    ]


    categories = {
        'cartoon' : {'posts' : cartoon},
        'anime' : {'posts' : anime},
        'movie' : {'posts' : movie},
        'video_games' : {'posts' : video_games},
    }

    for category, categoryData in categories.items():
        c = add_category(category)
        for p in categoryData['posts']:
            add_post(c, p['title'], p['likes'], p['views'] ,p['description'])


    for c in Category.objects.all():
        for p in Post.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_category(name):
    c = Category.objects.get_or_create(name = name)[0]
    c.save()
    return c

def add_post(category, title, likes, views ,description):
    p = Post.objects.get_or_create(category = category, title = title, description = description)[0]
    p.likes = likes
    p.views = views
    p.save()
    return p


if __name__ == '__main__':

    print('Starting Radar population script...')
    populate()
