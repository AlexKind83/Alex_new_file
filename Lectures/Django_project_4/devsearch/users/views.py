from django.shortcuts import render
from .models import Profile


def profiles(request):
    prof = Profile.objects.all()
    contex = {'profiles': prof}
    return render(request, 'users/index.html', contex)


def user_profile(request, pk):  # Профиль разработчика
    prof = Profile.objects.get(id=pk)

    top_skills = prof.skill_set.exclude(description__exact='')  # __exact = полное совпадение
    other_skills = prof.skill_set.filter(description='')

    contex = {'profile': prof,
              'top_skills': top_skills,
              'other_skills': other_skills,}
    return render(request, 'users/profile.html', contex)
