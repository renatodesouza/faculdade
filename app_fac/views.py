from json import detect_encoding
from sqlite3 import Cursor
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models.curso import Curso



class IndexView(ListView):
    model = Curso
    context_object_name = 'curso_list'
    template_name = 'app_fac/home.html'

    def get_queryset(self):
        return Curso.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['img1'] = Curso.objects.order_by('?')[:3]
        return context

class CursoDetailView(DetailView):
    model = Curso
    context_object_name = 'curso_list'
    template_name = 'app_fac/curso.html'

    def get_queryset(self):
        self.nome = get_object_or_404(Curso, pk=self.kwargs['pk'])
        return Curso.objects.filter(nome=self.nome)

    def get_context_data(self, **kwargs):
        context = super(CursoDetailView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        return context

class LoginView(TemplateView):
    template_name = 'app_fac/login.html'