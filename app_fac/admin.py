from dataclasses import fields
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm

from .models.my_user_admin import MyUserAdmin
from .models.aluno import Aluno
from .models.professor import Professor



@admin.register(MyUserAdmin)
class CustomUsuarioAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = MyUserAdmin

    fieldsset = (
        (None,                          {'fields': ('email', 'password')}),
        ('Informações Pessoais',        {'fields': ('first_name', 'last_name', 'dt_expiracao')}),
        ('Permissões',                  {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permission')}),
        ('Datas importantes',           {'fields': ('last_login', 'date_joined')},)
    )

    list_display = ('id', 'first_name', 'last_name', 'email', 'dt_expiracao', 'is_staff')

    def usuario(self, instance):
        return f'{instance.usuario.get_full_name}'

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados de usuario',                {'fields': ('usuario', 'ra', 'imagem')}),
        ('Contato',                         {'fields': ('celular',)}),
    ]

    list_display = ('id', 'usuario', 'celular', 'ra', 'imagem')

    def usuario(self, instance):
        return f'{instance.usuario.get_ful_name}'


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados de usuário',                {'fields':('usuario', 'rp', 'imagem')}),
        ('Contato',                         {'fields': ('celular',)})
    ]

    list_display = ('usuario', 'celular', 'rp', 'imagem')

    def usuario(self, instance):
        return f'{instance.usuario.get_full_name}'