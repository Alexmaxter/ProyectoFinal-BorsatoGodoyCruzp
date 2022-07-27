from collections import  UserList
from django.contrib.auth.models import User

from django.shortcuts import render

def inicio(request):

    users = User.objects.all()
    
    return render(request, "inicio.html",{"users":users})


