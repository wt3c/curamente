from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Sessao, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class ContatosSerializer(serializers.Serializer):
    telefone = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)


class SessoaSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Sessao
        fields = [
            "id",
            "user",
            "tipo",
            "horario",
            "perido",
            "desconforto_fisico",
            "desconforto_mental",
            "superado",
            "notas",

        ]
        depth = 1


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    contatos = ContatosSerializer()
    sessao = SessoaSerializer(many=True)

    class Meta:
        model = Profile
        fields = ["user", "tipo", "foto", "contatos", "sessao"]
