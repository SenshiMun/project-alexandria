# Generated by Django 4.2.3 on 2023-07-20 17:19

import alexandria_site.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('icon', models.ImageField(blank=True, upload_to='icons', verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'ODS',
                'verbose_name_plural': 'Objetivos',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='Sobre')),
                ('logo', models.ImageField(blank=True, upload_to='', verbose_name='Logo')),
                ('site', models.URLField(blank=True, verbose_name='Site')),
            ],
            options={
                'verbose_name': 'Parceiro',
                'verbose_name_plural': 'Parceiros',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Titulo')),
                ('slug', models.SlugField(max_length=20, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Conteúdo do Post')),
                ('date_posted', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('date_edited', models.DateField(auto_now=True, verbose_name='Data da Ultima Edição')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome do Projeto')),
                ('state', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='Estado')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('about', models.TextField(verbose_name='Sobre o Projeto')),
                ('cause', models.CharField(blank=True, max_length=30, verbose_name='Causa')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('image_1', models.ImageField(blank=True, upload_to=alexandria_site.models.Project.folder_name, verbose_name='Imagem')),
                ('image_2', models.ImageField(blank=True, upload_to=alexandria_site.models.Project.folder_name, verbose_name='Imagem')),
                ('image_3', models.ImageField(blank=True, upload_to=alexandria_site.models.Project.folder_name, verbose_name='Imagem')),
                ('image_4', models.ImageField(blank=True, upload_to=alexandria_site.models.Project.folder_name, verbose_name='Imagem')),
                ('image_5', models.ImageField(blank=True, upload_to=alexandria_site.models.Project.folder_name, verbose_name='Imagem')),
                ('image_6', models.ImageField(blank=True, upload_to=alexandria_site.models.Project.folder_name, verbose_name='Imagem')),
                ('video', models.FileField(blank=True, upload_to=alexandria_site.models.Project.folder_name, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Video')),
                ('ODS', models.ManyToManyField(to='alexandria_site.objective')),
                ('partners', models.ManyToManyField(to='alexandria_site.partner', verbose_name='Parceiros')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
        ),
    ]
