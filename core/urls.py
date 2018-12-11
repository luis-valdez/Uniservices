from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('lista_campus/', views.lista_campus, name='lista_campus'),
    path('lista_divisiones/<int:pk>/', views.lista_divisiones, name='lista_divisiones'),
    path('lista_servicios/<int:pk>/', views.lista_servicios, name='lista_servicios'),
    path('info_servicios/<int:pk>/', views.info_servicios, name='info_servicio'),
    path('mi_tutor/', views.mi_tutor, name='mi_tutor'),
    path('mis_alumnos/', views.mis_alumnos, name='mis_alumnos'),
    path('agendar_citas/', views.agendar_citas, name='agendar_citas'),
    path('mis_servicios/', views.mis_servicios, name='mis_servicios'),
    path('nuevo_servicio/', views.nuevo_servicio, name='nuevo_servicio'),
    

]