from django.contrib import admin
from . import models


class LivroAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'autor','pratileira','editora','classificacao']

admin.site.register(models.Livro,LivroAdmin)
admin.site.register(models.Categoria)