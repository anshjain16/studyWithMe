
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def Home(Request):
    return HttpResponse('Home Page')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home)
]
