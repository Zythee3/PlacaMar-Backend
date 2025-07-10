# api/models.py

from django.db import models

class Placa(models.Model):
    nome = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    subzona = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    embarcacoes = models.PositiveIntegerField()
    usuarios = models.PositiveIntegerField()
    cor = models.CharField(max_length=7)  # Ex: #FF0000
    descricao = models.TextField()

    def __str__(self):
        return self.nome
