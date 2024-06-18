from django.shortcuts import render, redirect
from .models import History
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    projects = History.objects.all()
    return render(request, 'russia_history/home.html', {'projects': projects})


def signupuser(request):
    if request.method == "GET":
        return render(request, 'russia_history/signupuser.html',
                  {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password2'])
                user.save()
                login(request, user)
                return redirect('customuser')
            except IntegrityError:
                return render(request, 'russia_history/signupuser.html',
                              {'form': UserCreationForm(), 'error': ""
                                                                    "Такое имя пользователя уже существует"})
        else:
            return render(request, 'russia_history/signupuser.html',
                          {'form': UserCreationForm(), 'error': "Пароли не совпадают"})


def customuser(request):
    return render(request, 'russia_history/customuser.html', )


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == "GET":
        return render(request, 'russia_history/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'russia_history/loginuser.html', {'form': AuthenticationForm(),
                          'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('customuser')
