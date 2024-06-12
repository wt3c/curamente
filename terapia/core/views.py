from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework import generics
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


class ProfileView(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.get(user__username=request.data.get("username"))
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        # profile = Profile.objects.get(user__username=request.data.get("username"))
        profile = Profile.objects.get(pk=10)
        usuario = request.data.pop("user")

        serializer = ProfileSerializer(profile, data=request.data)

        if serializer.is_valid():            
            serializer.save(usuario=usuario)
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class ProfileListView(generics.RetrieveUpdateDestroyAPIView):
    # serializer_class = MusicianSerializer
    # queryset = Musician.objects.all()
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
