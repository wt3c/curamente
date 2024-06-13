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


class PacienteSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    contatos = ContatosSerializer(read_only=True)
    sessao = SessoaSerializer(many=True, read_only=True)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(allow_null=True, required=False)
    contatos = ContatosSerializer()
    sessao = SessoaSerializer(many=True, allow_null=True, required=False)
    # paciente = PacienteSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "tipo", "pacientes", "foto", "contatos", "sessao"]

        def get_pacientes(self, obj):
            if obj.pacientes is not None:
                return ProfileSerializer(obj.pacientes).data
            else:
                return None

        depth = 2

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

    def update(self, instance, validated_data):
        """
            Update and return an existing `Profile` instance, given the validated data.
        """

        # ## Update user
        fields_user = validated_data.pop("usuario")
        instance.user.first_name = fields_user.get("first_name")
        instance.user.last_name = fields_user.get("last_name")
        instance.user.save()

        # ## Update Profile
        instance.tipo = validated_data.get("tipo")
        instance.foto = validated_data.get("foto")

        # ## Update Contatos
        instance.contatos.telefone = validated_data.get("contatos").get("telefone")
        instance.contatos.email = validated_data.get("contatos").get("email")
        instance.contatos.save()

        # ## Update Sessão 
        # instance.sessao.clear()
        for sessao in validated_data.get("sessao"):
            updated, created = Sessao.objects.update_or_create(
                id=sessao.get("id"),
                defaults={**sessao}
            )

            instance.sessao.add(updated)

        instance.save()

        return instance
