from django.contrib.gis.db import models

class Zona(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    restrita = models.BooleanField(default=False)
    geometria = models.PolygonField(srid=4326, null=True, blank=True)

    def __str__(self):
        return self.nome

class Subzona(models.Model):
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='subzonas')
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    atividades_permitidas = models.TextField(blank=True, null=True)
    atividades_proibidas = models.TextField(blank=True, null=True)
    geometria = models.PolygonField(srid=4326, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.zona.nome})"

class PontoDeInteresse(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    zona = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True, blank=True, related_name='pontos_de_interesse')

    def __str__(self):
        return self.nome

import uuid # Importar uuid

class QRCode(models.Model):
    code = models.CharField(max_length=255, unique=True, help_text="O código único do QR Code.")
    qr_code_value = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, help_text="Valor único para o QR Code físico.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.qr_code_value:
            self.qr_code_value = uuid.uuid4()
        super().save(*args, **kwargs)

class Placa(models.Model):
    subzona = models.ForeignKey(Subzona, on_delete=models.CASCADE, related_name='placas', null=True, blank=True)
    nome_placa = models.CharField(max_length=255, blank=True, null=True)
    localidade_x = models.CharField(max_length=255, blank=True, null=True)
    qr_code = models.OneToOneField(QRCode, on_delete=models.CASCADE, related_name='placa', null=True, blank=True, help_text="O QR Code associado a esta placa.")
    descricao = models.TextField(blank=True, null=True)
    acesso_restrito = models.BooleanField(default=False, help_text="Indica se o acesso a esta placa é restrito.")
    num_embarcacoes_desembarque = models.IntegerField(null=True, blank=True, help_text="Número de embarcações permitidas para embarque/desembarque.")
    max_pessoas_catamara = models.IntegerField(null=True, blank=True, help_text="Número máximo de pessoas por catamarã.")
    max_pessoas_miudas = models.IntegerField(null=True, blank=True, help_text="Número máximo de pessoas para embarcações miúdas.")
    atividades_autorizadas = models.JSONField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    ponto_interesse = models.ForeignKey(PontoDeInteresse, on_delete=models.SET_NULL, null=True, blank=True, related_name='placas')

    def __str__(self):
        return f"Placa {self.qr_code.code if self.qr_code else 'N/A'} ({self.subzona.nome})"

class Atividade(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome

class PlacaAtividade(models.Model):
    placa = models.ForeignKey(Placa, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('placa', 'atividade')
