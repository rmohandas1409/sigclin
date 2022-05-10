from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html
from django.db.models import Sum, Avg
from localflavor.br.br_states import STATE_CHOICES
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList
from django.contrib import admin

from django.contrib.auth.models import User


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Pacientes(Base):
    SEXO = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('indefinido', 'Indefinido'),

    )

    COR = (
        ('amarela', 'Amarela'),
        ('branca', 'Branca'),
        ('indigina', 'Indigina'),
        ('negra', 'Negra'),
        ('parda', 'Parda'),

    )

    ESTADO_CIVIL = (
        ('casado', 'Casado'),
        ('uniao-estavel', 'Uniao estavel'),
        ('desquitado', 'Desquitado'),
        ('divorciado', 'Divorciado'),
        ('outros', 'Outros'),
    )

    NACIONALIDADE = (
        ('brasileiro', 'Brasileiro'),
        ('estrangeiro', 'Estrangeiro'),
        ('outros', 'Outros'),
    )

    TIPO_LOGRADOURO = (
        ('rua', 'Rua'),
        ('avenida', 'Avenida'),
        ('outros', 'Outros'),
    )

    nome = models.CharField('Nome', max_length=200)
    nome_social = models.CharField('Nome Social', max_length=120)
    data_nascimento = models.DateField('Data de nascimento', max_length=11)
    sexo = models.CharField('Sexo', max_length=30, choices=SEXO)
    cor = models.CharField('Cor', max_length=30, choices=COR)
    identidade = models.CharField('N. Identitidade', max_length=50)
    orgao_emissor = models.CharField('Orgão Emissor', max_length=80)
    cpf = models.CharField('CPF', max_length=14, blank=True, default="XXX.XXX.XXX-XX")
    estado_civil = models.CharField('Estado Civil', max_length=30, choices=ESTADO_CIVIL)
    nacionalidade = models.CharField('Nacionalidade', max_length=30, choices=NACIONALIDADE)
    tipo_logradouro = models.CharField('Tipo Logradouro', max_length=30, choices=TIPO_LOGRADOURO)
    endereco = models.CharField('Endereço', max_length=80)
    numero = models.CharField('Numero', max_length=50)
    complemento = models.CharField('Complemento', max_length=50)
    bairro = models.CharField('Bairro', max_length=60)
    municipio = models.CharField('Municipio', max_length=50)
    estado = models.CharField('Estado', max_length=50)
    pais = models.CharField('Pais', max_length=100)
    cep = models.CharField('Cep', max_length=11)
    telefone = models.CharField('Telefone', max_length=15)
    celular = models.CharField('Celular', max_length=15)
    contato = models.CharField('Contato', max_length=80)
    nome_mae = models.CharField('Nome da mãe', max_length=80)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f'{self.nome} DN - {self.data_nascimento} - Mãe - {self.nome_mae}'


class Prontuario(Base):
    paciente = models.ForeignKey("Pacientes", on_delete=models.CASCADE)
    exame = models.ForeignKey("Exames", on_delete=models.CASCADE)
    altura = models.DecimalField('Altura', max_digits=5, decimal_places=2, blank=True)
    peso = models.DecimalField('Peso', max_digits=5, decimal_places=2, blank=True)
    pape = models.DecimalField('PAPE - mmHg', max_digits=5, decimal_places=2)
    fc = models.DecimalField('FC - bpm', max_digits=5, decimal_places=2)
    hgt = models.DecimalField('HGT', max_digits=5, decimal_places=2)
    creatinina = models.DecimalField(u'Dosagem de Creatinina - mg/dL0,31 mg/dL a 0,92 mg/dL', max_digits=5,
                                     decimal_places=2)
    potacio = models.DecimalField('Dosagem de Potássio - mmol/L3,50 mmol/L a 5,00 mmol/L', max_digits=5,
                                  decimal_places=2)
    ureia = models.DecimalField('Dosagem de Uréia  - mg/dL 15 mg/dL a 45 mg/dL', max_digits=5, decimal_places=2)
    # anamnse = models.TextField('Anamnse', blank=True)
    antecedentes_pessoais = models.TextField('Antecedentes pessoais', blank=True)
    comorbidades = models.TextField('Comorbidades', blank=True)
    medicamentos = models.TextField('Medicamentos em uso', blank=True)
    exames_fisicos = models.TextField('Exame Fisico', blank=True)
    conduta = models.TextField('Conduta', blank=True)
    retorno = models.TextField('Retorno', blank=True)
    obs = models.TextField('Observação')
    CATEGORY_CHOICES = (
        ('Liberado', 'Liberado'),
        ('Pendente', 'Pendente'),
        ('Bloqueado', 'Bloqueado'),
    )
    situacao = models.CharField(u'Situação', max_length=200, choices=CATEGORY_CHOICES)

    def imprimir(self):
        return mark_safe(
            """<a href=\"/pacientes/laudo/%s/\" target="_blank"><img src=\"/static/images/b_print.png\"></a>""" % self.id)

    class Meta:
        verbose_name = 'Prontuário'
        verbose_name_plural = 'Prontuários'

    def __str__(self):
        if self.paciente:
            return str(self.paciente)
        else:
            return self.custom_alias_name


class Especialidades(Base):
    especialidade = models.CharField("Especialidades", max_length=200)

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.especialidade


class Exames(Base):
    codigo = models.CharField("Codigo", max_length=80)
    exame = models.CharField("Exame", max_length=200)
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

    def __str__(self):
        return self.exame

