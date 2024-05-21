from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]

def home(Request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(Request, 'base/home.html', context)

def room(Request, pk):
    room = Room.objects.get(id = pk)
    
    context = {'room': room}
    return render(Request, 'base/room.html', context)