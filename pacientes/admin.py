from django import forms
from django.contrib import admin
from .models import Pacientes, Prontuario, Especialidades, Exames
from django.utils.html import format_html
from django.db.models import Sum, Avg


@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo', 'data_nascimento','telefone','celular','contato','ativo', 'criados', 'modificado')
    search_fields = ('nome',)
    list_per_page = 30
    date_hierarchy = 'criados'
    save_on_top = True

@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):

    #search_fields = ('paciente',)
    list_per_page = 30
    save_on_top = True
    list_display = ('paciente', 'exame', 'status', 'imprimir', 'ativo', 'criados', 'modificado')

    def status(self, obj):
        if obj.situacao == 'Liberado':
            color = 'green'
        elif obj.situacao == 'Pendente':
            color = 'orange'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situacao))

    status.allow_tags = True


@admin.register(Especialidades)
class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ('especialidade', 'ativo', 'criados', 'modificado')

@admin.register(Exames)
class ExamesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'exame', 'valor', 'ativo', 'criados', 'modificado')