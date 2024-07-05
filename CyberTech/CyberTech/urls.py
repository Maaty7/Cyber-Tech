from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name="principal"),
    path('Tecnologia', views.tecnologia, name="tecnologia"),
    path('Hardware', views.hardware, name="hardware"),
    path('Perifericos', views.perifericos, name="perifericos"),
    path('Electrodomesticos', views.electrodomesticos, name="electrodomesticos"),
    path('VistaProducto', views.vistaProducto, name="vistaProducto"),
    path('Registro', views.registro, name="registro"),
]
