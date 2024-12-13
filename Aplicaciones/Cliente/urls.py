from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_ciudad/', views.listar_ciudad, name='listar_ciudad'),
    path('insertar_ciudad/', views.insertar_ciudad, name='insertar_ciudad'),
    path('obtener_ciudad/<int:id>/', views.obtener_ciudad, name='obtener_ciudad'),
    path('actualizar_ciudad/', views.actualizar_ciudad, name='actualizar_ciudad'),
    path('eliminar_ciudad/<int:id>/', views.eliminar_ciudad, name='eliminar_ciudad'),
]