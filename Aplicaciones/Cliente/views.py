from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Ciudad, Propietario

# Create your views here.
def home(request):
    return render(request, 'home.html')

def listar_ciudad(request):
    getCiudad = Ciudad.objects.all()
    return render(request, 'Ciudad/listar_ciudad.html', {'ciudad':getCiudad})

def insertar_ciudad(request):
    nombre = request.POST['nombre'].upper()
    nueva_ciudad = Ciudad.objects.create(nombre_ciu = nombre)
    return redirect('listar_ciudad')

def obtener_ciudad(request, id):
    ciudad = get_object_or_404(Ciudad, id_ciu=id)
    data = {
        'id_ciu': ciudad.id_ciu,
        'nombre_ciu': ciudad.nombre_ciu
    }
    return JsonResponse(data)

def actualizar_ciudad(request):
    id = request.POST['id_act']
    nombre = request.POST['nombre_act'].upper()
    
    ciudad = get_object_or_404(Ciudad, id_ciu=id)
    ciudad.nombre_ciu = nombre
    ciudad.save()
    return redirect('listar_ciudad')

def eliminar_ciudad(request, id):
    ciudad = get_object_or_404(Ciudad, id_ciu=id)
    ciudad.delete()
    return redirect('listar_ciudad')
