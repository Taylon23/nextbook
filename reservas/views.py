from django.shortcuts import render
from . import forms 
from . import models
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')

@login_required
def agendar_livro(request, livro_id):
    livro = models.Livros.objects.get(pk=livro_id)
    
    if request.method == 'POST':
        form = forms.AgendamentoLivroForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.livro = livro
            agendamento.usuario = request.user  # Define o usuário automaticamente
            agendamento.save()
    else:
        form = forms.AgendamentoLivroForm()
    
    return render(request, 'agendar_livro.html', {'form': form, 'livro': livro})
