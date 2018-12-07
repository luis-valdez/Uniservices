from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('lista_campus/', views.lista_campus, name='lista_campus'),
    path('lista_divisiones/<int:pk>/', views.lista_divisiones, name='lista_divisiones'),
    path('lista_servicios/<int:pk>/', views.lista_servicios, name='lista_servicios'),
    path('info_servicios/<int:pk>/', views.info_servicios, name='info_servicio'),
    path('post/new/', views.post_new, name='post_new'),
]