from django.contrib.gis.db import models

class Area(models.Model):
    name = models.CharField(max_length=255)
    geom = models.PolygonField(srid=4326)

    def __str__(self):
        return self.name
