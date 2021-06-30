from rest_framework import serializers
from core.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =['user','email','nombre','apellido','fechaDeNacimiento','clave','categoria']

        