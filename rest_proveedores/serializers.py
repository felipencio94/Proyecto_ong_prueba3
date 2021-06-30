from rest_framework import serializers
from core.models import Proveedor

class ProveedorForm(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields =['rut','nombreProveedor','descripcion','telefono','emailProveedor','tipoServicio']