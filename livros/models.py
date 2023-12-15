from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.categoria}'

    def save(self, *args, **kwargs):
        # Garantir que a primeira letra da categoria seja maiúscula
        self.categoria = self.categoria.capitalize()
        super(Categoria, self).save(*args, **kwargs)


class Livro(models.Model):
    img_livro = models.ImageField(
        upload_to='img_livro/', verbose_name='imagem do livro')
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    sinopse = models.TextField()
    local = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    ano = models.IntegerField()
    pratileira = models.IntegerField()
    volume = models.IntegerField()
    quantidade_exemplares = models.IntegerField(
        verbose_name='Livros disponíveis')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    classificacao = models.IntegerField(verbose_name='classificação')
    sob_demanda = models.BooleanField(default=False)
    favoritado = models.BooleanField(default=False)

    def __str__(self):
        return f'Livro: {self.titulo} - Autor: {self.autor}  - Volume: {self.editora}'


@receiver(pre_delete, sender=Livro)
def delete_livro_image(sender, instance, **kwargs):
    # Verifica se a instância do livro tem uma imagem associada a ela
    if instance.img_livro:
        # Exclui o arquivo de imagem quando o livro é excluído
        if os.path.isfile(instance.img_livro.path):
            os.remove(instance.img_livro.path)
