from django.contrib.auth.models import User
from django.db import models

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='Usuário')
    nome = models.CharField('Nome', max_length=128)
    data_de_nascimento = models.DateField('Data de nascimento',blank=True,null=True)
    telefone_celular = models.CharField('Telefone celular', max_length=15,help_text='Formato (99) 99999-9999', null=True,blank=True)
    telefone_fixo = models.CharField('Telefone fixo', max_length=15,help_text='Formato (99) 99999-9999', null=True,blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Noticia(models.Model):
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
    titulo = models.CharField('Título',max_length=128, blank=True, null=True)
    conteudo = models.TextField()
    autor = models.ForeignKey(Pessoa,on_delete=models.CASCADE, null=True,blank=True,verbose_name='Autor')
    data_publicacao = models.DateField('Data', blank=True, null=True)
    
    def __str__(self):
        return self.titulo

class Tag(models.Model):
    nome = models.CharField('Tag',max_length=64)
    slug = models.SlugField('Slug',max_length=64)
    noticias = models.ManyToManyField(Noticia)

    def __str__(self):
        return self.nome