
from django.db import models
# Create your models here.

class filmes(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class atores(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class elenco(models.Model):
    name = models.CharField(max_length=100)
    filmes = models.ForeignKey('filmes', on_delete=models.CASCADE, related_name='filmes')
    atores = models.ForeignKey('atores', on_delete=models.CASCADE, related_name='atores')
    def __str__(self):
        return self.name





