from django.shortcuts import render
from AcercaDeApp.models import Empleado

def acerca_de(request):

    empleados= Empleado.objects.all()
    return render(request, "AcercaDeApp/acerca_de.html", {"empleados":empleados})
