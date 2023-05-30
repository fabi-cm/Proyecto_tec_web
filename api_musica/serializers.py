from rest_framework import serializers
from .models import Cancion, Genero, PerfilUsuario, Usuario
from django.contrib.auth.models import User


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"


class CancionSerializer(serializers.ModelSerializer):
    # genero = GeneroSerializer(many=True)

    class Meta:
        model = Cancion
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","email","password"]


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PerfilUsuario
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)

        perfil_usuario = PerfilUsuario.objects.create(user=user, **validated_data)

        return perfil_usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"