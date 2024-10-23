from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home, name='home'),
    path('insert/', views.insertData, name='insert')
]