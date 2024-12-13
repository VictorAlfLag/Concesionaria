from django.contrib import messages
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Ciudad, Propietario, Color, Modelo, Vehiculo, Factura

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

def listar_color(request):
    getColor = Color.objects.all()
    return render(request, 'Color/listar_color.html', {'color': getColor})

def insertar_color(request):
    nombre = request.POST['nombre'].upper()
    nuevo_color = Color.objects.create(nombre_col=nombre)
    messages.success(request, "Color registrado correctamente.")
    return redirect('listar_color')

def obtener_color(request, id):
    color = get_object_or_404(Color, id_col=id)
    data = {
        'id_col': color.id_col,
        'nombre_col': color.nombre_col
    }
    return JsonResponse(data)

def actualizar_color(request):
    id = request.POST['id_act']
    nombre = request.POST['nombre_act'].upper()
    
    color = get_object_or_404(Color, id_col=id)
    color.nombre_col = nombre
    color.save()
    messages.success(request, "Color actualizado correctamente.")
    return redirect('listar_color')

def eliminar_color(request, id):
    color = get_object_or_404(Color, id_col=id)
    color.delete()
    messages.success(request, "Color eliminado correctamente.")
    return redirect('listar_color')


def listar_modelo(request):
    getModelo = Modelo.objects.all()
    return render(request, 'Modelo/listar_modelo.html', {'modelo': getModelo})

def insertar_modelo(request):
    nombre = request.POST['nombre'].upper()
    nuevo_modelo = Modelo.objects.create(nombre_mod=nombre)
    messages.success(request, "Modelo registrado correctamente.")
    return redirect('listar_modelo')

def obtener_modelo(request, id):
    modelo = get_object_or_404(Modelo, id_mod=id)
    data = {
        'id_mod': modelo.id_mod,
        'nombre_mod': modelo.nombre_mod
    }
    return JsonResponse(data)

def actualizar_modelo(request):
    id = request.POST['id_act']
    nombre = request.POST['nombre_act'].upper()
    
    modelo = get_object_or_404(Modelo, id_mod=id)
    modelo.nombre_mod = nombre
    modelo.save()
    messages.success(request, "Modelo actualizado correctamente.")
    return redirect('listar_modelo')

def eliminar_modelo(request, id):
    modelo = get_object_or_404(Modelo, id_mod=id)
    modelo.delete()
    messages.success(request, "Modelo eliminado correctamente.")
    return redirect('listar_modelo')

def listar_vehiculo(request):
    getVehiculo = Vehiculo.objects.all()
    getModelo = Modelo.objects.all()
    getColor = Color.objects.all()
    return render(request, 'Vehiculo/listar_vehiculo.html', { 'vehiculo': getVehiculo, 'modelo': getModelo, 'color': getColor })

def insertar_vehiculo(request):
    anio = request.POST.get('anio')
    placa = request.POST.get('placa').upper()
    modelo_id = request.POST.get('modelo')
    color_id = request.POST.get('color')

    modelo = get_object_or_404(Modelo, id_mod=modelo_id)
    color = get_object_or_404(Color, id_col=color_id)

    nuevo_Vehiculo = Vehiculo.objects.create(anio_veh=anio, placa_veh=placa, fkid_mod=modelo, fkid_col=color)

    messages.success(request, "Vehículo registrado correctamente.")
    return redirect('listar_vehiculo')

def obtener_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id_veh=id)
    data = {
        'id_veh': vehiculo.id_veh,
        'anio_veh': vehiculo.anio_veh,
        'placa_veh': vehiculo.placa_veh,
        'fkid_mod': vehiculo.fkid_mod.id_mod,
        'fkid_col': vehiculo.fkid_col.id_col,
    }
    return JsonResponse(data)

def actualizar_vehiculo(request):
    id = request.POST.get('id_act')
    anio = request.POST.get('anio_act')
    placa = request.POST.get('placa_act').upper()
    modelo_id = request.POST.get('modelo_act')
    color_id = request.POST.get('color_act')

    modelo = get_object_or_404(Modelo, id_mod=modelo_id)
    color = get_object_or_404(Color, id_col=color_id)

    vehiculo = get_object_or_404(Vehiculo, id_veh=id)
    vehiculo.anio_veh = anio
    vehiculo.placa_veh = placa
    vehiculo.fkid_mod = modelo
    vehiculo.fkid_col = color
    vehiculo.save()

    messages.success(request, "Vehículo actualizado correctamente.")
    return redirect('listar_vehiculo')

def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id_veh=id)
    vehiculo.delete()
    messages.success(request, "Vehículo eliminado correctamente.")
    return redirect('listar_vehiculo')

def listar_factura(request):
    facturas = Factura.objects.all()
    propietarios = Propietario.objects.all()
    vehiculos = Vehiculo.objects.all()
    return render(request, 'Factura/listar_factura.html', {
        'facturas': facturas,
        'propietarios': propietarios,
        'vehiculos': vehiculos
    })

def insertar_factura(request):
    precio = request.POST.get('precio')
    propietario_id = request.POST.get('fkid_pro')
    vehiculo_id = request.POST.get('fkid_veh')

    propietario = get_object_or_404(Propietario, id_pro=propietario_id)
    vehiculo = get_object_or_404(Vehiculo, id_veh=vehiculo_id)

    nueva_factura = Factura.objects.create(precio_fac=precio, fkid_pro=propietario, fkid_veh=vehiculo)

    messages.success(request, "Factura registrada correctamente.")
    return redirect('listar_factura')

def obtener_factura(request, id):
    factura = get_object_or_404(Factura, id_fac=id)
    data = {
        'id_fac': factura.id_fac,
        'precio_fac': factura.precio_fac,
        'fkid_pro': factura.fkid_pro.id_pro,
        'fkid_veh': factura.fkid_veh.id_veh,
    }
    return JsonResponse(data)

def actualizar_factura(request):
    id = request.POST.get('id_act')
    precio = request.POST.get('precio_act')
    propietario_id = request.POST.get('fkid_pro_act')
    vehiculo_id = request.POST.get('fkid_veh_act')

    propietario = get_object_or_404(Propietario, id_pro=propietario_id)
    vehiculo = get_object_or_404(Vehiculo, id_veh=vehiculo_id)

    factura = get_object_or_404(Factura, id_fac=id)
    factura.precio_fac = precio
    factura.fkid_pro = propietario
    factura.fkid_veh = vehiculo
    factura.save()

    messages.success(request, "Factura actualizada correctamente.")
    return redirect('listar_factura')

def eliminar_factura(request, id):
    factura = get_object_or_404(Factura, id_fac=id)
    factura.delete()
    messages.success(request, "Factura eliminada correctamente.")
    return redirect('listar_factura')
