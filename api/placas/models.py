from django.db import models

class Placa(models.Model):
    nome_placa = models.CharField(max_length=255)
    subzona = models.CharField(max_length=50)
    localidade = models.CharField(max_length=100)
    embarcacoes = models.IntegerField()
    usuarios = models.IntegerField()
    cor = models.CharField(max_length=7)
    descricao = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nome_placa
