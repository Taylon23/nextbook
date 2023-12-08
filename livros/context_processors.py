from . import models


def categorias_globais(request):
    categorias = models.Categoria.objects.all()
    livros = models.Livro.objects.all()
    return {'categorias': categorias,'livros': livros,}