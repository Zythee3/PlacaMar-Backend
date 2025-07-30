from django.db import models

class Estado(models.Model):
    uf = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='cidades')
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        unique_together = ('estado', 'nome')
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} - {self.estado.uf}"
