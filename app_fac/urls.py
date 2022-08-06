from re import template
from django.urls import path
from .views import IndexView, TestView


app_name = 'app_fac'

urlpatterns = [
    path('home/', IndexView.as_view(template_name='app_fac/home.html'), name='home'),
    path('teste/', TestView.as_view(template_name='app_fac/teste.html'), name='teste'),
] 