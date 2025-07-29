from django.contrib.gis.db import models

class Placa(models.Model):
    nome_placa = models.CharField(max_length=255)
    localidade = models.CharField(max_length=255, blank=True, null=True)
    zona = models.CharField(max_length=255, blank=True, null=True)
    atividades_permitidas = models.TextField(blank=True, null=True)
    qtd_placas = models.IntegerField(default=1)
    descricao = models.TextField(blank=True, null=True)
    num_embarcacoes = models.IntegerField(default=0)
    max_pessoas_catamara = models.IntegerField(default=0)
    max_pessoas_miudas = models.IntegerField(default=0)
    location = models.PointField(srid=4326)  # coordenadas geográficas

    def __str__(self):
        return self.nome_placa
