from django.contrib.gis.db import models

class Zona(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    regras = models.TextField(blank=True, null=True)
    restrita = models.BooleanField(default=False)
    geometria = models.PolygonField(srid=4326)

    def __str__(self):
        return self.nome

class PontoDeInteresse(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    zona = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True, blank=True, related_name='pontos_de_interesse')

    def __str__(self):
        return self.nome

class Placa(models.Model):
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='placas')
    codigo_qr = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)
    atividades_autorizadas = models.JSONField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    ponto_interesse = models.ForeignKey(PontoDeInteresse, on_delete=models.SET_NULL, null=True, blank=True, related_name='placas')

    def __str__(self):
        return self.codigo_qr

class Atividade(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome

class PlacaAtividade(models.Model):
    placa = models.ForeignKey(Placa, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('placa', 'atividade')
