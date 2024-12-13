from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_vehiculos/', views.listar_propietario, name='listar_vehiculos'),
]