from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=25)
    year = models.PositiveSmallIntegerField()
    paradigm = models.CharField(max_length=50)
    site = models.URLField()


