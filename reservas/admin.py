from django.contrib import admin
from . import models


class AgendamentoLivroAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'data_agendamento', 'entregue')
    list_filter = ('entregue',)
    actions = ['marcar_como_entregue', 'desmarcar_como_entregue']

    def marcar_como_entregue(self, request, queryset):
        queryset.update(entregue=True)
        for agendamento in queryset:
            agendamento.livro.quantidade_livros += 1
            agendamento.livro.save()

    marcar_como_entregue.short_description = "Marcar como Entregue"

    def desmarcar_como_entregue(self, request, queryset):
        queryset.update(entregue=False)
        for agendamento in queryset:
            if agendamento.livro.quantidade_livros > 0:
                agendamento.livro.quantidade_livros -= 1
                agendamento.livro.save()

    desmarcar_como_entregue.short_description = "Desmarcar como Entregue"


admin.site.register(models.Livros)
admin.site.register(models.Categoria)

admin.site.register(models.AgendamentoLivro, AgendamentoLivroAdmin)
