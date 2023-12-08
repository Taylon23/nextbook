from django.shortcuts import render, get_object_or_404
from . import models
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# @login_required(login_url="")
def home(request):
    livros_em_alta = models.Livro.objects.filter(sob_demanda=True)
    return render(request, 'home.html', {'em_alta': livros_em_alta})


def base(request):
    return render(request, 'home.html')


def search_book(request):
    query = request.GET.get('q')
    categoria_id = request.GET.get('categoria')
    livros = models.Livro.objects.all()

    if query:
        livros = livros.filter(Q(titulo__icontains=query)
                               | Q(autor__icontains=query))

    if categoria_id:
        livros = livros.filter(categoria_id=categoria_id)

    return render(request, 'search_results_book.html', {'livros': livros, 'query': query})


def profile_book(request, id):
    livro = models.Livro.objects.filter(id=id)
    return render(request, 'profile_results_book.html', {'livro': livro, })
