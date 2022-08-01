from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import curso



class IndexView(TemplateView):
    template_name = 'app_fac/home.html'