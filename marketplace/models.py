from django.db import models
from django.contrib.gis.db import models as gis_models

class ComunidadeLocal(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    localizacao_base = gis_models.PointField(srid=4326, null=True, blank=True)
    contato_email = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

class ParceiroB2B(models.Model):
    usuario = models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE, related_name='parceiro_b2b')
    nome_negocio = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True, blank=True, null=True)
    categoria = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome_negocio

class ProdutosMarketplace(models.Model):
    parceiro_b2b = models.ForeignKey(ParceiroB2B, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    comunidade = models.ForeignKey(ComunidadeLocal, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class TransacaoMarketplace(models.Model):
    produto = models.ForeignKey(ProdutosMarketplace, on_delete=models.CASCADE, related_name='transacoes')
    comprador_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='compras')
    data_transacao = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status_pagamento = models.CharField(max_length=50, default='Pendente')
    comissao_plataforma = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Transação {self.id} - {self.produto.nome}"

class RoteiroTuristico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    comunidade = models.ForeignKey(ComunidadeLocal, on_delete=models.SET_NULL, null=True, blank=True, related_name='roteiros')
    tipo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

class RoteiroPontoInteresse(models.Model):
    roteiro = models.ForeignKey(RoteiroTuristico, on_delete=models.CASCADE)
    ponto_interesse = models.ForeignKey('zonas.PontoDeInteresse', on_delete=models.CASCADE)
    ordem = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('roteiro', 'ponto_interesse')
