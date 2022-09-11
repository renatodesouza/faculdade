from re import template
from unicodedata import name
from django.urls import path
from .views import IndexView, CursoDetailView, LoginView, AlunoView, ExtView, AlunoDetailView


app_name = 'app_fac'

urlpatterns = [
    path('', IndexView.as_view(template_name='app_fac/home.html'), name='home'),
    path('login/', LoginView.as_view(template_name='app_fac/login.html'), name='login'),
    path('curso/<int:pk>/', CursoDetailView.as_view(template_name='app_fac/curso.html'), name='curso'),
    # path('aluno/', AlunoView.as_view(template_name='app_fac/aluno.html'), name='aluno'),
    path('aluno/<int:pk>/', AlunoDetailView.as_view(template_name='app_fac/aluno.html'), name='aluno'),
    path('ext/', ExtView.as_view(template_name='app_fac/exte.html'), name='ext')
] 