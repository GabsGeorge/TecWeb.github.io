# coding=utf-8

from django.urls import reverse
from django.db import models

class Fornecedor(models.Model):
    nome_f = models.CharField(db_column='Nome_F', unique=True, max_length=100)  # Field name made lowercase.
    email_f = models.CharField(db_column='Email_F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    endereco_f = models.CharField(db_column='Endereco_F', max_length=255)  # Field name made lowercase.
    telefoneprincipal = models.IntegerField(db_column='TelefonePrincipal')  # Field name made lowercase.
    telefonesecundario = models.IntegerField(db_column='TelefoneSecundario', blank=True, null=True)  # Field name made lowercase.
    categoria_f = models.CharField(db_column='Categoria_F', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return self.nome_f

    class Meta:
        managed = True
        db_table = 'Fornecedor'

class Categoria(models.Model):
    nome = models.CharField("Nome" ,max_length=100)
    slug = models.SlugField("Identificador", max_length=100)
    criado = models.DateTimeField("Criado em", auto_now_add=True)
    modificado = models.DateTimeField("modificado em", auto_now_add=True)
    imagem = models.ImageField(db_column='Imagem',upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'Categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def get_absolute_url(self):
        return reverse('categoria', kwargs={'slug': self.slug})       

class Produto(models.Model):
    codigo_p = models.AutoField(db_column='Codigo_P', primary_key=True)  # Field name made lowercase.
    nome_f = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='Nome Fornecedor')  # Field name made lowercase.
    nome_p = models.CharField("Nome do produto", db_column='Nome_P', max_length=100)  # Field name made lowercase.
    quantidade = models.SmallIntegerField("Quantidade", db_column='Quantidade')  # Field name made lowercase.
    categoria_p = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_p')  # Field name made lowercase.
    imagem = models.ImageField("Imagem", db_column='Imagem',upload_to='media')
    descricao = models.TextField("Descrição",db_column='Descricao_P')
    custo_p = models.DecimalField("Custo", decimal_places=2, max_digits=10, db_column='Custo_P')
    preco_p = models.DecimalField("Preço", decimal_places=2, max_digits=10, db_column='Preço_P')
    #altura = models.DecimalField("Altura em cm", decimal_places=2, max_digits=10, db_column='alutra')
    #largura = models.DecimalField("largura em cm", decimal_places=2, max_digits=10, db_column='largura')
    #comprimeito = models.DecimalField("comprimeito em cm", decimal_places=2, max_digits=10, db_column='comprimeito')
    
    slug = models.SlugField("Identificador", max_length=100)
    vender = models.BooleanField(db_column='Vender', default=True)
    ativo = models.BooleanField(db_column='Ativo',default=True)
    criado = models.DateTimeField("Criado em", auto_now_add=True)
    modificado = models.DateTimeField("modificado em", auto_now_add=True)

    def __str__(self):
        return self.nome_p

    class Meta:
        managed = True
        db_table = 'Produto'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome_p']  

    def get_absolute_url(self):
        return reverse('produto', kwargs={'slug': self.slug})      