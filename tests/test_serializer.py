import pytest
from terapia.core import serializer
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from terapia.core.models import Profile, Contatos, Sessao


@pytest.fixture
def create_profile():
    user = User.objects.create(username="admin", password="admin123")
    contatos = Contatos.objects.create(telefone="123456789", email="admin@gmail.com")
    sessao = Sessao.objects.create(horario="2024-11-01T10:00:00Z")
    profile = Profile.objects.create(user=user, tipo="admin", foto="admin.jpg", contatos=contatos)
    profile.sessao.add(sessao)
    return profile


class TestProfileSerializer(APITestCase):
    def test_serializer_create(self, create_profile):
        profile_data = {
            "user": {"username": "test", "password": "test123"},
            "tipo": "test",
            "foto": "test.jpg",
            "contatos": {"telefone": "987654321", "email": "test@gmail.com"},
            "sessao": [{"horario": "2024-11-02T10:00:00Z"}]
        }

        serializer = serializer.ProfileSerializer(data=profile_data)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()

        assert profile.user.username == "test"
        assert profile.tipo == "test"
        assert profile.foto == "test.jpg"
        assert profile.contatos.telefone == "987654321"
        assert "2024-11-02T10:00:00Z" in [sessao.horario for sessao in profile.sessao.all()]

    def test_serializer_update(self, create_profile):
        profile_data = {
            "user": {"first_name": "John", "last_name": "Doe"},
            "tipo": "updated",
            "foto": "updated.jpg",
            "contatos": {"telefone": "111222333", "email": "updated@gmail.com"},
            "sessao": [{"horario": "2024-11-03T10:00:00Z"}]
        }

        serializer = serializer.ProfileSerializer(instance=create_profile, data=profile_data, partial=True)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()

        assert profile.user.first_name == "John"
        assert profile.user.last_name == "Doe"
        assert profile.tipo == "updated"
        assert profile.foto == "updated.jpg"
        assert profile.contatos.telefone == "111222333"
        assert "2024-11-03T10:00:00Z" in [sessao.horario for sessao in profile.sessao.all()]
