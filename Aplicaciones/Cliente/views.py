from django.contrib import messages
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
    messages.success(request, "Ciudad registrado correctamente.")
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
    messages.success(request, "Ciudad actualizado correctamente.")
    return redirect('listar_ciudad')

def eliminar_ciudad(request, id):
    ciudad = get_object_or_404(Ciudad, id_ciu=id)
    ciudad.delete()
    messages.success(request, "Ciudad eliminado correctamente.")
    return redirect('listar_ciudad')

def listar_propietario(request):
    getPropietario = Propietario.objects.all()
    getCiudad = Ciudad.objects.all()
    return render(request, 'Propietario/listar_propietario.html', { 'propietario':getPropietario, 'ciudad':getCiudad })

def insertar_propietario(request):
    nombre = request.POST.get('nombre').upper()
    apellido = request.POST.get('apellido').upper()
    correo = request.POST.get('correo')
    telefono = request.POST.get('telefono')
    ciudad_id = request.POST.get('ciudad')
    
    ciudad = get_object_or_404(Ciudad, id_ciu=ciudad_id)
    
    nuevo_Propietario = Propietario.objects.create(nombre_pro = nombre, apellido_pro = apellido, email_pro = correo, telefono_pro = telefono, fkid_ciu = ciudad)
    
    messages.success(request, "Personal registrado correctamente.")
    return redirect('listar_propietario')

def obtener_propietario(request, id):
    propietario = get_object_or_404(Propietario, id_pro=id)
    data = {
        'id_pro': propietario.id_pro,
        'nombre_pro': propietario.nombre_pro,
        'apellido_pro': propietario.apellido_pro,
        'email_pro': propietario.email_pro,
        'telefono_pro': propietario.telefono_pro,
        'fkid_ciu': propietario.fkid_ciu.id_ciu,
    }
    return JsonResponse(data)

def actualizar_prpietario(request):
    id = request.POST.get('id_act')
    nombre = request.POST.get('nombre_act').upper()
    apellido = request.POST.get('apellido_act').upper()
    correo = request.POST.get('correo_act')
    telefono = request.POST.get('telefono_act')
    ciudad_id = request.POST.get('ciudad_act')
    
    ciudad = get_object_or_404(Ciudad, id_ciu=ciudad_id)
    
    propietario = get_object_or_404(Propietario, id_pro=id)
    propietario.nombre_pro = nombre
    propietario.apellido_pro = apellido
    propietario.email_pro = correo
    propietario.telefono_pro = telefono
    propietario.fkid_ciu = ciudad
    propietario.save()
    
    messages.success(request, "Personal actualizado correctamente.")
    return redirect('listar_propietario')

def eliminar_propietario(request, id):
    propietario = get_object_or_404(Propietario, id_pro=id)
    propietario.delete()
    messages.success(request, "Personal eliminado correctamente.")
    return redirect('listar_propietario')
