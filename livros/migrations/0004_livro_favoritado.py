# Generated by Django 4.1.12 on 2023-12-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_livro_sob_demanda'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='favoritado',
            field=models.BooleanField(default=False),
        ),
    ]
