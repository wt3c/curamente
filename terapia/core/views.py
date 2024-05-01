from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import authenticate
from rest_framework.views import APIView


def homepage(request):
    return render(request, 'core/index.html')


class login(APIView):

    def post(self, request):
        pass


def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.get('username'), password=request.get('password'))
        if user is not None:
            auth_login(request, user)
            return redirect('/')
    else:
        return render(request, 'core/core_home.html')


def home_core(request):
    return render(request, 'core/core_home.html')
