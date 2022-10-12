from re import template
from unicodedata import name
from django.urls import path
from .views import IndexView, CursoDetailView, LoginView, AlunoView, ExtView, AlunoDetailView


app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(template_name='app/home.html'), name='home'),
    path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),
    path('curso/<int:pk>/', CursoDetailView.as_view(template_name='app/curso.html'), name='curso'),
    # path('aluno/', AlunoView.as_view(template_name='app/aluno.html'), name='aluno'),
    path('aluno/<int:pk>/', AlunoDetailView.as_view(template_name='app/aluno.html'), name='aluno'),
    path('ext/', ExtView.as_view(template_name='app/exte.html'), name='ext')
] 