from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Sessao, Profile, Contatos


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
    user = UserSerializer()
    contatos = ContatosSerializer()
    sessao = SessoaSerializer(many=True)

    class Meta:
        model = Profile
        fields = ["user", "tipo", "foto", "contatos", "sessao"]

    def create(self, validated_data):
        fields_user = validated_data.get("user")
        user = User.objects.create_user(
            password=make_password(fields_user.get("password")),
            **validated_data.pop("user")
        )

        contatos_data = validated_data.pop("contatos")
        contatos = Contatos.objects.create(**contatos_data)
        validated_data["contatos"] = contatos

        sessao_list = validated_data.pop("sessao")

        profile = Profile.objects.create(user=user, **validated_data)

        for sessao in sessao_list:
            sessao_id = Sessao.objects.create(**sessao)
            profile.sessao.add(sessao_id)

        return profile
