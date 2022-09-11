from dis import dis
from json import detect_encoding
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from app_fac.models.disciplina_ofertada import DisciplinaOfertada

from app_fac.models.my_user_admin import MyUserAdmin
from .models.curso import Curso
from .models.aluno import Aluno
from .models.matricula import Matricula
from .models.atividade_vinculada import AtividadeVinculada



class IndexView(ListView):
    model = Curso
    context_object_name = 'curso_list'
    template_name = 'app_fac/home.html'

    def get_queryset(self):
        return Curso.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
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
        context['curso'] = Curso.objects.get(nome=self.nome)
        context['destaques'] = Curso.objects.get(id=self.nome.id)
        # context['coordenador'] = Curso.objects.get(nome__coordenador)
        return context

class LoginView(TemplateView):
    template_name = 'app_fac/login.html'

class AlunoView(TemplateView):
    template_name = 'app_fac.aluno.html'

class AlunoDetailView(DetailView):
    model = Aluno
    context_object_name = 'aluno_list'
    template_name = 'app_fac/aluno.html'

    def get_queryset(self):
        self.user = get_object_or_404(MyUserAdmin, pk=self.kwargs['pk'])
        return MyUserAdmin.objects.filter(id__exact=self.user.id)

    def get_context_data(self, **kwargs):
        context = super(AlunoDetailView, self).get_context_data(**kwargs)
        context['aluno'] = Aluno.objects.get(usuario__email=self.user)
        context['list_aluno'] = Matricula.objects.get(aluno__usuario=self.user) 
        context['disciplinas'] = DisciplinaOfertada.objects.filter(curso=context['list_aluno'].curso)
        context['atividades'] = AtividadeVinculada.objects.filter\
        (disciplina_ofertada__turma=context['list_aluno'].turma).filter(disciplina_ofertada=2)
        context['aluno_all'] = Matricula.objects.get(aluno__usuario=self.user)
        
        
        return context

class ExtView(TemplateView):
    template_name = 'app_fac.exte.html'