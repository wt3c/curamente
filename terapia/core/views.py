from django.contrib.auth import authenticate
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from terapia.core.models import Profile, Sessao
from terapia.core.serializer import ProfileSerializer, SessoaSerializer


class Login(APIView):
    def post(self, request, format=None):

        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))

        if user:
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class UsuarioView(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.get(user__username=request.data.get("username"))
        terapeuta = profile.pacientes.all()
        serializer = ProfileSerializer(terapeuta, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)

        pacientes = request.data.pop("pacientes")

        if serializer.is_valid():
            serializer.save(pacientes=pacientes)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        pass


class UsuarioDetail(APIView):
    def get(self, request, pk, format=None):
        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        serializer = ProfileSerializer(data=request.data)
        therapist = Profile.objects.get(pk=pk)
        # After authentication feature, compare id with authenticated user to validate patient creation.

        if(therapist.tipo.lower() != "terapeuta"):
            content = {'message' : 'id inválido'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            new_patient = serializer.save(pacientes=[])
            therapist.pacientes.add(new_patient)
            therapist.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = Profile.objects.get(pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        profile = Profile.objects.get(pk=pk)
        usuario = request.data.pop("user")
        sessao = request.data.pop("sessao")
        pacientes = request.data.pop("pacientes")

        serializer = ProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save(usuario=usuario, sessao=sessao, pacientes=pacientes)
            return Response(serializer.data)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
class SessaoView(APIView):
    def get(self, request, pk, format=None):
        patient = get_object_or_404(Profile, pk=pk)
        sessions = patient.sessao.all()
        serializer = SessoaSerializer(sessions, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        patient = get_object_or_404(Profile, pk=pk)
        sessions = request.data.pop("sessao")

        new_session = SessoaSerializer(data=sessions)

        if new_session.is_valid():
            created_session = new_session.save()
            patient.sessao.add(created_session)
            return Response(new_session.data)
            
        return Response(new_session.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        session = get_object_or_404(Sessao, pk=pk)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        session = get_object_or_404(Sessao, pk=pk)
        update = request.data.pop("sessao")

        serializer = SessoaSerializer(session, data=update, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    