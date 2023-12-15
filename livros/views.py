from django.shortcuts import render, get_object_or_404
from . import models
from django.http import Http404
from usuarios import models as models_user
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def home(request):
    livros_em_alta = models.Livro.objects.filter(sob_demanda=True)
    categorias_interesse = ['Artes e fotografia',
                            'Infantil e juvenil', 'Ficção', 'Aventura']
    livros_por_categoria = {}

    for categoria_nome in categorias_interesse:
        try:
            categoria = models.Categoria.objects.get(categoria=categoria_nome)
            livros_categoria = models.Livro.objects.filter(
                categoria=categoria)[:8]
            livros_por_categoria[categoria] = livros_categoria
        except models.Categoria.DoesNotExist:
            raise Http404("Categoria não encontrada")

    return render(request, 'home.html', {'em_alta': livros_em_alta, 'livros_por_categoria': livros_por_categoria})


def base(request):
    return render(request, 'home.html')


def search_book(request):
    query = request.GET.get('q')
    categoria_id = request.GET.get('categoria')
    livros = models.Livro.objects.all()

    if query:
        livros = livros.filter(Q(titulo__icontains=query)
                               | Q(autor__icontains=query) | Q(editora__icontains=query))

    if categoria_id:
        livros = livros.filter(categoria_id=categoria_id)

    # Definindo o número de itens por página
    itens_por_pagina = 8
    paginator = Paginator(livros, itens_por_pagina)

    page_number = request.GET.get('page')
    try:
        livros_pagina = paginator.page(page_number)
    except PageNotAnInteger:
        # Se a página não for um número inteiro, vá para a primeira página
        livros_pagina = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo, retorne a última página disponível
        livros_pagina = paginator.page(paginator.num_pages)

    return render(request, 'search_results_book.html', {'livros': livros_pagina, 'query': query})


def profile_book(request, id):
    livro = get_object_or_404(models.Livro, id=id)
    esta_favoritado = False  # Inicialmente, assume que não está favoritado

    if request.user.is_authenticated:
        # Verifica se o livro está na lista de favoritos do usuário logado
        esta_favoritado = models_user.Favorito.objects.filter(
            usuario=request.user, livro=livro).exists()

    return render(request, 'profile_results_book.html', {'profile': livro, 'esta_favoritado': esta_favoritado})
