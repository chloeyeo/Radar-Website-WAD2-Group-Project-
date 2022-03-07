from django.shortcuts import render
from django.http import HttpResponse
from radar.forms import UserForm, UserProfileForm


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
