from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.response import Response

from terapia.core.models import Profile
from terapia.core.serializer import ProfileSerializer


class Login(APIView):
    def post(self, request, format=None):

        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))

        if user:
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class TerapeutaView(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.get(user__username=request.data.get("username"))
        terapeuta = profile.pacientes.all()
        serializer = ProfileSerializer(terapeuta, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        # PK_TERAPEUTA = 1
        # list_pacienete = [id_2, id_5]        

        # tera = Profile.objects.get(pk=PK_TERAPEUTA)
        # 
        # for paciente in List_pacienete:
        #     user = User.objects.get(pk=paciente)
        #     tera.pacientes.add(user)     

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        pass


class PacienteView(APIView):
    def get(self, request, pk, format=None):
        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        profile = Profile.objects.get(pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        profile = Profile.objects.get(pk=pk)
        usuario = request.data.pop("user")
        sessao = request.data.pop("sessao")

        serializer = ProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save(usuario=usuario, sessao=sessao)
            return Response(serializer.data)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
