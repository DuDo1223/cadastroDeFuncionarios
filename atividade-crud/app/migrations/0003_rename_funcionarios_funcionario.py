# Generated by Django 4.1.13 on 2024-12-03 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_cliente_funcionarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Funcionarios',
            new_name='Funcionario',
        ),
    ]
