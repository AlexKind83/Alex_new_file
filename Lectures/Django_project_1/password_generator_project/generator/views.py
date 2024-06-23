from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    lst = list(range(6, 15))
    # print(lst)
    return render(request, 'generator/home.html', {'lst': lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]  # Символы нижнего регистра ASCII.

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])  # Символы верхнего регистра ASCII.

    if request.GET.get('number'):
        char.extend([chr(i) for i in range(48, 58)])  # Добавляем цифры регистра ASCII.

    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])  # Добавляем спец символы регистра ASCII.

    psw = ''
    # print(char)
    length = int(request.GET.get('length'))  # Так как приходит строка нужно перевести в число.
    for i in range(length):  # Добавляем количество символов от-по.
        psw += random.choice(char)
    return render(request, 'generator/password.html', {'password': psw})


def document(request):
    return render(request, 'generator/documentation.html')
