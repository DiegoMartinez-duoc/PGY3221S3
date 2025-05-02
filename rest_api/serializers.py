from rest_framework import serializers
from core.models import ThreadUser, CredencialesUsuario, Thread

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadUser
        fields = ['nombre', 'nombre_usuario', 'fecha_nacimiento']


class CredencialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CredencialesUsuario
        fields = ['email', 'contrasena', 'rol']


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['nombre_thread', 'imagen', 'mensaje', 'usuario']



class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['mensaje', 'usuario', 'thread']
        