from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'radar/index.html')

def about(request):
    return render(request, 'radar/about.html')


def homepage1(request):
    return render(request, 'radar/homepage1.html')

def homepage2(request):
    return render(request, 'radar/homepage2.html')

def friendspage(request):
    return render(request, 'radar/friendspage.html')

def login(request):
    return render(request, 'radar/login.html')

def signup(request):
    return render(request, 'radar/signup.html')

def account(request):
    return render(request, 'radar/account.html')
    
