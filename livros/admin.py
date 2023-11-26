from django.contrib import admin
from . import models


class LivroAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'autor']

admin.site.register(models.Livro,LivroAdmin)
admin.site.register(models.Categoria)