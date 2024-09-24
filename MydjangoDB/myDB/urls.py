from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('insertData',views.insertData, name='insertData'),
    path('delete/<int:id>/', views.delete_customer, name='deleteCustomer'),
]