from django.shortcuts import render
from .models import Tecnologia, Hardware, Periferico, Electrodomestico
# Create your views here.

def principal(request):
    context = {}
    return render(request, "pages/principal.html", context)

def tecnologia(request):
    tecnologia = Tecnologia.objects.all()
    context = {
        'tecnologia' : tecnologia
    }
    return render(request, "pages/tecnologia.html", context)

def hardware(request):
    hardware = Hardware.objects.all()
    context = {
        'hardware' : hardware
    }
    return render(request, "pages/hardware.html", context)

def perifericos(request):
    periferico = Periferico.objects.all()
    context = {
        'periferico' : periferico
    }
    return render(request, "pages/perifericos.html", context)

def electrodomesticos(request):
    electrodomesticos = Electrodomestico.objects.all()
    context = {
        'electro' : electrodomesticos
    }
    return render(request, "pages/electrodomesticos.html", context)

def vistaProducto(request):
    context = {}
    return render(request, "pages/vistaProductos.html", context)

def registro(request):
    context = {}
    return render(request, "pages/registro.html", context)
