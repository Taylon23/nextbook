from django.db import models
from django.contrib.auth.models import User
from livros import models as models_livros


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(models_livros.Livro, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Usuario: {self.usuario} - Anuncio: {self.livro.titulo}'