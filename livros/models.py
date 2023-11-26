from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.categoria}'


class Livro(models.Model):
    img_livro = models.ImageField(
        upload_to='img_livro/', verbose_name='imagem do livro')
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    sinopse = models.TextField()
    local = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    ano = models.IntegerField()
    volume = models.IntegerField()
    quantidade_exemplares = models.IntegerField(verbose_name='Livros disponíveis')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    classificacao = models.IntegerField(verbose_name='classificação')


    def __str__(self):
        return f'Livro: {self.titulo} - Autor: {self.autor}  - Volume: {self.editora}'
