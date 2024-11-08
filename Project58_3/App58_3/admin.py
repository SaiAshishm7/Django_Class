from django.contrib import admin
from .models import PersonalInfo, Experience, Education, Skill

admin.site.register(PersonalInfo)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)