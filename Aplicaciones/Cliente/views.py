from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def listar_propietario(request):
    return render(request, 'Propietarios/listar_vehiculos.html')