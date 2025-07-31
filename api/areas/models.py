from django.contrib.gis.db import models

class AreaPermitida(models.Model):
    nome = models.CharField(max_length=255)
    geom = models.PolygonField()

    def __str__(self):
        return self.nome