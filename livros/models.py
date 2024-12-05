from django.db import models

# Create your models here.

class Livro(models.Model):
  titulo = models.CharField(max_length=200)
  autor = models.CharField(max_length=100)
  editora = models.CharField(max_length=100)
  ano_publicacao = models.IntegerField()
  isbn = models.CharField(max_length=13)
  descricao = models.TextField()

  def __str__(self):
    return self.titulo