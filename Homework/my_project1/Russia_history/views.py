from django.shortcuts import render
from .models import History


def home(request):
    projects = History.objects.all()
    return render(request, 'russia_history/home.html', {'projects': projects})
