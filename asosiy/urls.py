from django.urls import path
from . import views

urlpatterns = [
    path('', views.Asosiy, name = 'asosiy'),
    path('malumot/', views.Malumot, name = 'malumot'),
    path('aloqa/', views.Aloqa, name='aloqa'),
    path('yangiliklar/', views.Yangiliklar, name = 'yangiliklar'),
    path('joylar/', views.Joylar, name = 'joylar'),
    path('qidiruv/', views.Qidiruv, name = 'qidiruv'),
    path('royxatdan-otish', views.RoyxatdanUtish, name='royxatdan-utish'),
]