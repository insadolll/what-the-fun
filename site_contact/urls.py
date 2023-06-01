from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_list, name='site_list'),
    path('site/create/', views.site_create, name='site_create'),
    path('site/<int:site_id>/', views.site_detail, name='site_detail'),
    path('site/<int:site_id>/update/', views.site_update, name='site_update'),
    path('site/<int:site_id>/delete/', views.site_delete, name='site_delete'),
    path('site/<int:site_id>/contact/create/', views.contact_create, name='contact_create'),
    path('site/<int:site_id>/contact/<int:contact_id>/update/', views.contact_update, name='contact_update'),
    path('site/<int:site_id>/contact/<int:contact_id>/delete/', views.contact_delete, name='contact_delete'),
]