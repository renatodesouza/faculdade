from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm

from .models.my_user_admin import MyUserAdmin



@admin.register(MyUserAdmin)
class CustomUsuarioAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = MyUserAdmin

    fields_set = (
        (None,                          {'fields': ('email', 'password')}),
        ('Informações Pessoais',        {'fields': ('first_name', 'last_name', 'dt_expiracao')}),
        ('Permissões',                  {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permission')}),
        ('Datas importantes',           {'fields': ('last_login', 'date_joined')},)
    )

    list_display = ('id', 'first_name', 'last_name', 'email', 'dt_expiracao', 'is_staff')

    def usuario(self, instance):
        return f'{instance.usuario.get_full_name}'