from re import template
from unicodedata import name
from django.urls import path
from .views import IndexView, CursoDetailView, LoginView


app_name = 'app_fac'

urlpatterns = [
    path('home/', IndexView.as_view(template_name='app_fac/home.html'), name='home'),
    path('login/', LoginView.as_view(template_name='app_fac/login.html'), name='login'),
    path('curso/<int:pk>/', CursoDetailView.as_view(template_name='app_fac/curso.html'), name='curso'),
] 