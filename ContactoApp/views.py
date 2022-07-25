from django.shortcuts import render

def contacto(request):
    
    return render(request, "ContactoApp/contacto.html")