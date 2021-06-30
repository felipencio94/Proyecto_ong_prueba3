from django.urls import path
from rest_proveedores.views import lista_proveedores,modificar_proveedores,actualizar_proveedores
urlpatterns = [
    path('proveedores', lista_proveedores, name="lista_proveedores"),
    path('proveedor', modificar_proveedores, name="modificar_proveedores"),
    path('proveedor/<id>', actualizar_proveedores, name="actualizar_proveedores"),
]