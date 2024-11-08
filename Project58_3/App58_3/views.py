from django.shortcuts import render
from .models import PersonalInfo, Experience, Education, Skill

def home(request):
    context = {
        'personal_info': PersonalInfo.objects.first(),
        'experiences': Experience.objects.all().order_by('-start_date'),
        'education': Education.objects.all().order_by('-graduation_date'),
        'skills': Skill.objects.all(),
    }
    return render(request, 'home.html', context)