from django.shortcuts import render

def inicio(request):

    
    return render(request, "inicio.html")

def tienda(request):

    return render(request, "tienda.html")

