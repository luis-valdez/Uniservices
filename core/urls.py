from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('inicia_sesion/', views.login, name='inicia_sesion'),
]