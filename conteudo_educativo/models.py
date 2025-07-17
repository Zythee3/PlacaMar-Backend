from django.db import models

class ConteudoEducativo(models.Model):
    titulo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    conteudo = models.TextField()
    topico = models.CharField(max_length=255, blank=True, null=True)
    ponto_interesse = models.ForeignKey('zonas.PontoDeInteresse', on_delete=models.SET_NULL, null=True, blank=True, related_name='conteudos_educativos')
    zona = models.ForeignKey('zonas.Zona', on_delete=models.SET_NULL, null=True, blank=True, related_name='conteudos_educativos')

    def __str__(self):
        return self.titulo
