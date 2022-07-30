from django.shortcuts import render

def acerca_de(request):

    # empleados= Empleado.objects.all()
    return render(request, "AcercaDeApp/acerca_de.html", {})
