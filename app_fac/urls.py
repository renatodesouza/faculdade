from re import template
from django.urls import path
from .views import IndexView


app_name = 'app_fac'

urlpatterns = [
    path('home/', IndexView.as_view(template_name='app_fac/home.html'), name='home'),
] 