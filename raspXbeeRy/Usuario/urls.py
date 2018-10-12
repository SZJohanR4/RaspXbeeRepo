from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Conexiones', views.conexiones, name='conexiones'),
    path('Sistema', views.sistema, name='sistema'),
    path('Red', views.red, name='red'),
]
