# Generated by Django 4.1.12 on 2023-12-07 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='pratileira',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
