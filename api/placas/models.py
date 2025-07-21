from django.contrib.gis.db import models

class Placa(models.Model):
    nome_placa = models.CharField(max_length=255)
    localidade = models.CharField(max_length=255)
    zona = models.CharField(max_length=255)
    atividades_permitidas = models.TextField(blank=True, null=True)
    qtd_placas = models.IntegerField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    num_embarcacoes = models.IntegerField(blank=True, null=True)
    max_pessoas_catamara = models.IntegerField(blank=True, null=True)
    max_pessoas_miudas = models.IntegerField(blank=True, null=True)
    # Campo geográfico PointField para latitude/longitude
    location = models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return self.nome_placa
