from django.db import models

class Noticia(models.Model):
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
    titulo = models.CharField('título',max_length=128, blank=True, null=True)
    conteudo = models.TextField()
    autor = models.CharField('Autor',max_length=128, blank=True, null=True)
    data_publicacao = models.DateField('Data', blank=True, null=True)
    def __str__(self):
        return self.titulo