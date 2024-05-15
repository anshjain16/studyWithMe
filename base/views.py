from django.shortcuts import render
from django.http import HttpResponse

def home(Request):
    return HttpResponse('Home Page')

def room(Request):
    return HttpResponse('Rooms')