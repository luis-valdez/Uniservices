# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup/estudiante/', views.EstudianteSignUpView.as_view(), name='estudiante_signup'),
    path('signup/tutor/', views.TutorSignUpView.as_view(), name='tutor_signup'),
]