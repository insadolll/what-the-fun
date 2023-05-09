from django.urls import path
from . import views

urlpatterns = [
    path('', views.ipaddr, name='ipaddr'),
    path('add/', views.ipaddr_add, name='ipaddr_add'),
    path('<int:pk>/edit/', views.ipaddr_edit, name='ipaddr_edit'),
    path('<int:pk>/delete/', views.ipaddr_delete, name='ipaddr_delete'),
]
