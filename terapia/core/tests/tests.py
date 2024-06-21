from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from terapia.core.models import Profile
from terapia.core.serializer import ProfileSerializer


class ProfileAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.contatos_data = {"telefone": "123456", "email": "testuser@gmail.com"}
        self.sessao_data = [{"title": "Sessao1", "description": "Sessao Description"}]
        self.profile_data = {
            "user": self.user.id,  # for serializer we pass `id` instead of `user` instance
            "tipo": "tipo1",
            "pacientes": [],
            "foto": "foto.jpg",
            "contatos": self.contatos_data,
            "sessao": self.sessao_data
        }

    def test_profile_serializer_create(self):
        serializer = ProfileSerializer(data=self.profile_data)
        self.assertTrue(serializer.is_valid())
        profile = serializer.save()
        self.assertIsInstance(profile, Profile)
        self.assertEqual(profile.user, self.profile_data["user"])
        self.assertEqual(profile.tipo, self.profile_data["tipo"])
        self.assertEqual(profile.foto, self.profile_data["foto"])
        self.assertEqual(profile.contatos.telefone, self.profile_data["contatos"]["telefone"])
        self.assertEqual(profile.contatos.email, self.profile_data["contatos"]["email"])
        self.assertEqual(profile.sessao.get().title, self.profile_data["sessao"][0]["title"])
        self.assertEqual(profile.sessao.get().description, self.profile_data["sessao"][0]["description"])

    def test_profile_serializer_update(self):
        serializer = ProfileSerializer(data=self.profile_data)
        self.assertTrue(serializer.is_valid())
        profile = serializer.save()
        updated_data = {
            "user": self.user.id,  # for serializer we pass `id` instead of `user` instance
            "tipo": "updatedtipo",
            "foto": "updatedfoto.jpg",
            "contatos": {"telefone": "789012", "email": "updatedmail@gmail.com"},
            "sessao": [{"title": "Updated Sessao", "description": "Updated Description"}]
        }
        new_serializer = ProfileSerializer(profile, data=updated_data, partial=True)
        
        # Print errors to console if not valid
        if not new_serializer.is_valid():
            print(new_serializer.errors)

        self.assertTrue(new_serializer.is_valid())
        updated_profile = new_serializer.save()
        self.assertEqual(updated_profile.user, updated_data["user"])
        self.assertEqual(updated_profile.tipo, updated_data["tipo"])
        self.assertEqual(updated_profile.foto, updated_data["foto"])
        self.assertEqual(updated_profile.contatos.telefone, updated_data["contatos"]["telefone"])
        self.assertEqual(updated_profile.contatos.email, updated_data["contatos"]["email"])
        self.assertEqual(updated_profile.sessao.get().title, updated_data["sessao"][0]["title"])
        self.assertEqual(updated_profile.sessao.get().description, updated_data["sessao"][0]["description"])
