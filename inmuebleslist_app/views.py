from django.shortcuts import render
from inmuebleslist_app.models import Inmueble
from django.http import JsonResponse

# Create your views here.

def inmueble_list(request):
    #This function returns all Inmueble objects as a JSON response.
    inmuebles = Inmueble.objects.all() 
    data = {
        'inmuebles': list(inmuebles.values())
    } # Se define como diccionario para usar la clase JsonResponse
    
    return JsonResponse(data)

def inmueble_detalle(request, pk):
    inmueble = Inmueble.objects.get(pk=pk)
    data = {
        'direccion': inmueble.direccion,
        'pais': inmueble.pais,
        'imagen': inmueble.imagen,
        'activo': inmueble.activo,
        'descripcion': inmueble.descripcion
    }
    
    return JsonResponse(data)
    