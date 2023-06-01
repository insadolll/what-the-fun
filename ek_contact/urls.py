from django.urls import path
from . import views

urlpatterns = [
    path('', views.ek_contact_list, name='ek_contact_list'),
]
