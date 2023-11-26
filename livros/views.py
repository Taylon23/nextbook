from django.shortcuts import render,get_object_or_404
from . import models
from django.db.models import Q 
from django.contrib.auth.decorators import login_required

# @login_required(login_url="")
def home(request):
    livros = models.Livro.objects.all()
    categorias = models.Categoria.objects.all()
    return render(request,'home.html',{'livros':livros,'categorias': categorias})

def search_book(request):
    query = request.GET.get('q')
    categoria_id = request.GET.get('categoria')
    livros = models.Livro.objects.all()

    if query:
        livros = livros.filter(Q(titulo__icontains=query) | Q(autor__icontains=query))

    if categoria_id:
        livros = livros.filter(categoria_id=categoria_id)

    return render(request, 'search_results_book.html', {'livros': livros, 'query': query})
