from django.urls import path,include
from .views import index, contacto, proveedores, seccion_gatos, seccion_perros, form_nuevoProv, form_modProv, form_delProv
from django import urls

urlpatterns = [
    path('', index, name="inicio"),
    path('contacto', contacto, name="contacto.html"),
    path('proveedores', proveedores, name='proveedores.html'),
    path('seccion-gatos', seccion_gatos, name="seccion_gatos.html"),
    path('seccion-perros', seccion_perros, name="seccion_perros.html"),
    path('form_nuevoProv', form_nuevoProv, name="form_nuevoProv" ),
    path('form_modProv/<id>', form_modProv, name="form_modProv"),
    path('form_delProv/<id>', form_delProv, name="form_delProv")
]