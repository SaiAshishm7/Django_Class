from django.urls import path
from . import views

app_name = 'App_58'

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate/', views.calculate_bmi, name='calculate'),
]