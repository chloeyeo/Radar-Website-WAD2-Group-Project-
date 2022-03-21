import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'radar_project.settings')

import django
django.setup()
from radar.models import Category, Post
from django.contrib.auth.models import User
from django.core.files.images import ImageFile

def populate():
    cartoon = [
        {'title' : 'Krusty krab', 'views': 12, 'likes':10, 'image' : "/images/KrustyKrab.jpg", 'description':'The Krusty Krab is a fictional fast food restaurant in the American animated television series SpongeBob SquarePants. It is famous for its signature burger, the Krabby Patty, the formula to which is a closely guarded trade secret.'},
        {'title' : 'Enchated Forest','views':24, 'likes':15, 'image': "/images/frozen.jpg", 'description':"Olaf. The Enchanted Forest is a location in Disney's 2019 animated feature film Frozen II. It is a dense, magical forest inhabited by the spirits of nature, and the Northuldra people."},
        {'title' : "Rupanzel's Tower",'views':17, 'likes':12, 'image': "/images/RupanzelsTower.jpg", 'description' : "Rapunzel's Tower is a central location in Disney's 2010 animated feature film, Tangled. It is a secluded tower hidden deep within the woods outside of the kingdom Corona. Shortly after her birth, Princess Rapunzel was kidnapped by a woman named Mother Gothel, and locked away in the tower as an unknowing prisoner for eighteen years."},
        {'title' : "Gru's House" , 'views':46, 'likes':42, 'image': "/images/gru.jpg", 'description' :"Gru's House is home of Felonius Gru, Lucy Wilde, Margo, Edith, Agnes, and also to the Minions, Dr. Nefario and Dru. Gru's lab is located right underneath. Unlike the neighboring track houses (homes that appear similar to others), it is made out of brick that is painted eerie black and a roof that is painted purple. It is also somewhat considerably larger. One similiarity it does share is that it is a two-story house."},
    ]

    anime = [
        {'title' : "Hawk's mum" ,'views':19, 'likes':14, 'image': "/images/Hawksmum.jpg", 'description':'After rebuilding the Boar Hat, Hawk Mama is responsible for transporting the Seven Deadly Sins and Elizabeth to their next mission in Corand.'},
        {'title' : 'Avatar Temple' ,'views':23, 'likes':35, 'image': "/images/AvatarTemple.jpg", 'description' :"An Avatar Temple is a shrine built in honor of the Avatar. Each building bears a spiritual connection with the Avatar Spirit and all of its past incarnations, and as such is regarded as a sacrosanct dwelling. Some nations take this reverence for the Avatar Temple to an extreme, only permitting their respective religious authority to have regular access. For example, the Avatar Temple of the Air Nomads was open exclusively to the elder monks,[1] and only Fire Sages resided in the Fire Temple.[2] However, the Avatar is exempt from these restrictions."},
        {'title' : "Howl's Moving Castle" ,'views':18, 'likes':19, 'image': "/images/Howls.jpg",'description' : "The castle is actually Howl, it has different faces and lots of baggage which makes it heavy, it moves around to keep hidden, metaphors for a man who presents different faces to the world and keeps his true self hidden because of past hurt."},
        {'title' : 'Bathhouse' , 'views':72, 'likes':60, 'image': "/images/Bathhouse.jpg", 'description' :"The Bathhouse, which stands on a half-dried swamp is a very grandiose and opulent structure on the island Yūya in the Spirit Realm. Built in a traditional Japanese bathhouse style, its color scheme encompasses shades of red, green and semi-dark tones of brown. A waterfall is also present at its bridge crossing."},
    ]

    movie = [
        {'title' : 'Horgwats' , 'views':54, 'likes':35, 'image': "/images/hogwarts-castle.jpg",'description' : 'Hogwarts School of Witchcraft and Wizardry, often shortened to Hogwarts, was the British wizarding school, located in the Scottish Highlands.It accepted magical students from Great Britain and Ireland for enrolment.It was a state-owned school, funded by the Ministry of Magic.'},
        {'title' : 'Avengers Tower' , 'views':32, 'likes':25, 'image': "/images/AvengersTower.jpg",'description':'Avengers Tower is a fictional location in the Marvel Cinematic Universe. It was the original headquarters of the Avengers.'},
        {'title' : 'Kamar-Taj' , 'views':37, 'likes':29, 'image': "/images/Kamar-Taj.jpg",'description' : "Kamar-Taj - a mythical Tibetan city hidden in the Himalayan mountains where Doctor Strange receives his training as Sorcerer Supreme - is a rather textbook case of that second type, being a more-or-less direct lift of Shangri-La, the similarly mystical city at the center of James Hilton's classic novel Lost Horizon."},
        {'title' : 'Atlantis' , 'views':59, 'likes':50, 'image': "/images/Atlantis.jpg", 'description' :"Atlantis, a fabulously wealthy and advanced civilization, was swept into the sea and lost forever."},
    ]

    video_games = [
        {'title' : 'WarZone - Verdansk Hospital ' , 'views':54, 'likes':35, 'image': "/images/verdansk.jpg",'description' : "Verdansk Hospital is a little section located at the top right of Verdansk Southwest which is surrounded by a large open area that you’ll want to avoid walking in as it’ll make you an easy target. Here you can find the best loot inside the Hospital, but it is pretty low elsewhere. There are five vehicles scattered around the place and an ammo cache in the building beside the Burger Town."},
        {'title' : 'God of War - Regions and Realms' , 'views':32, 'likes':25, 'image': "/images/realms.jpg",'description':"Midgard is one of the Nine Realms and is the realm Kratos currently calls home. It's also the main area you will explore in God of War. The following summary encompasses all of the regions found in Midgard."},
        {'title' : 'PUBG - Erangel' , 'views':37, 'likes':29, 'image': "/images/pubg.jpg",'description' : "PUBG is a player versus player shooter game in which up to one hundred players fight in a battle royale, a type of large-scale last man standing deathmatch where players fight to remain the last alive. Players can choose to enter the match solo, duo, or with a small team of up to four people."},
        {'title' : 'Identity V - Waiting Room' , 'views':59, 'likes':50, 'image': "/images/identityv.jpg", 'description' :"Identity V is a 1v4 asymmetrical survival horror game by NetEase which is currently available for IOS and Android. With a Burtonesque style, gothic visuals, and a suspenseful storyline, it brings a new gaming experience to players. Fear Always Springs from the Unknown."},
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
            add_post(c, p['title'], p['likes'], p['views'] ,p['description'], p['image'])


    for c in Category.objects.all():
        for p in Post.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_category(name):
    c = Category.objects.get_or_create(name = name)[0]
    c.save()
    return c

def add_post(category, title, likes, views ,description, image):
    p = Post.objects.get_or_create(category = category, title = title, description = description)[0]
    p.likes = likes
    p.views = views
    # read image in binary
    p.image = image
    p.save()
    return p


if __name__ == '__main__':

    print('Starting Radar population script...')
    populate()
