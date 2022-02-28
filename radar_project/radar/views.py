from django.shortcuts import render
from django.http import HttpResponse

def index(reques):
    return HttpResponse("Radar says lets start")
