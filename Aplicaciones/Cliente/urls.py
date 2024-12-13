from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_propietario/', views.listar_propietario, name='listar_propietario'),
]