from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Pacientes, Prontuario, Exames
from .forms import *

class LaudoView(TemplateView):
    template_name = 'paciente.html'

    def get_context_data(self, id=None, *args, **kwargs):
        context = super(LaudoView, self).get_context_data(**kwargs)
        context['laudo_base'] = Prontuario.objects.get(id=id)

        return context


def exames_new(request):
    if request.method == "POST":
        form = ExameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('exames_edit', pk=post.pk)
    else:
        form = ExameForm()
    return render(request, 'cad_exames.html', {'form': form})


def exames_edit(request, pk):
    post = get_object_or_404(Exames, pk=pk)
    if request.method == "POST":
        form = ExameForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('exames_edit', pk=post.pk)
    else:
        form = ExameForm(instance=post)
    return render(request, 'edit_exames.html', {'form': form})

