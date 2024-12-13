from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_ciudad/', views.listar_ciudad, name='listar_ciudad'),
    path('insertar_ciudad/', views.insertar_ciudad, name='insertar_ciudad'),
    path('obtener_ciudad/<id>/', views.obtener_ciudad, name='obtener_ciudad'),
    path('actualizar_ciudad/', views.actualizar_ciudad, name='actualizar_ciudad'),
    path('eliminar_ciudad/<id>/', views.eliminar_ciudad, name='eliminar_ciudad'),
    path('listar_propietario/', views.listar_propietario, name='listar_propietario'),
    path('insertar_propietario/', views.insertar_propietario, name='insertar_propietario'),
    path('obtener_propietario/<id>/', views.obtener_propietario, name='obtener_propietario'),
    path('actualizar_prpietario/', views.actualizar_prpietario, name='actualizar_prpietario'),
    path('eliminar_propietario/<id>', views.eliminar_propietario, name='eliminar_propietario'),
    
    
]