from django.db import models

class ConteudoEducativo(models.Model):
    titulo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    conteudo = models.TextField()
    topico = models.CharField(max_length=255, blank=True, null=True)
    placa = models.ForeignKey('zonas.Placa', on_delete=models.SET_NULL, null=True, blank=True, related_name='conteudos_educativos')
    quiz_data = models.JSONField(blank=True, null=True, help_text="Dados do quiz: perguntas, opções e respostas.")

    def __str__(self):
        return self.titulo
