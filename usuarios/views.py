from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from .forms import SignUpForm
from . import models
from livros import models as model_livro
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'singup.html', {'form': form})


@login_required(login_url='login')
def meus_favoritos(request):
    favoritos = models.Favorito.objects.filter(usuario=request.user)
    # Dividindo em páginas, 10 itens por página
    paginator = Paginator(favoritos, 8)
    # Obtendo o número da página da query string, padrão é a página 1
    page_number = request.GET.get('page')

    # Obtendo os objetos da página atual
    page_obj = paginator.get_page(page_number)
    return render(request, 'livros_favoritos.html', {'page_obj': page_obj})

@login_required(login_url='login')
def favoritar_livro(request, livro_id):
    livro = get_object_or_404(model_livro.Livro, pk=livro_id)

    if request.user.is_authenticated:
        favorito, created = models.Favorito.objects.get_or_create(
            usuario=request.user, livro=livro)
        if not created:
            favorito.delete()
        livro.favoritado = not livro.favoritado
        livro.save()
        return JsonResponse({'status': 'ok'})
    else:
        login_url = reverse('login')  # Obtém a URL de login
        return JsonResponse({'status': 'error', 'message': 'Usuário não autenticado', 'login_url': login_url})
