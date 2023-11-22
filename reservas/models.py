from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    
    def __str__(self):
        return self.categoria


class Livros(models.Model):
    nome = models.CharField(max_length=50)
    img_livro = models.ImageField(
        upload_to='img_livro/', verbose_name='imagem do livro')
    sinopse = models.TextField()
    autor = models.CharField(max_length=50)
    volume = models.IntegerField()
    quantidade_livros = models.IntegerField(verbose_name='Livros disponíveis')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return f'Livro: {self.nome} - Volume: {self.volume} - Autor: {self.autor}'


class AgendamentoLivro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    data_agendamento = models.DateField()
    entregue = models.BooleanField(default=False)

    def __str__(self):
        return f'Usuário: {self.usuario.username} - Livro: {self.livro.nome} - Volume: {self.livro.volume} Data: {self.data_agendamento}'


@receiver(post_save, sender=AgendamentoLivro)
def atualizar_quantidade_livros_agendados(sender, instance, created, **kwargs):
    if created:  # Verifica se é um novo agendamento
        livro_agendado = instance.livro
        livro_agendado.quantidade_livros -= 1
        livro_agendado.save()


@receiver(pre_save, sender=AgendamentoLivro)
def atualizar_quantidade_livros_entregues(sender, instance, **kwargs):
    try:
        old_instance = AgendamentoLivro.objects.get(pk=instance.pk)
    except AgendamentoLivro.DoesNotExist:
        return

    if old_instance.entregue and not instance.entregue:
        livro_agendado = instance.livro
        livro_agendado.quantidade_livros -= 1
        livro_agendado.save()
    elif not old_instance.entregue and instance.entregue:
        livro_agendado = instance.livro
        livro_agendado.quantidade_livros += 1
        livro_agendado.save()
