# coding=utf-8
import os
from django.db import models


class WingManufact(models.Model):
    # Fabricants d'ailes

    # Les images seront stockées dans un sous répertoire avec l'id du fabricant
    def getImagePath(self, filename):
        path = os.path.join(os.path.join('wings-manufact', str(self.user.id)), filename)
        return path

    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to=getImagePath, blank=True)
    created_at = models.DateTimeField(verbose_name="Created on", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Edited on", auto_now=True)

    def __unicode__(self):
        return self.name


class Wing(models.Model):
    # Voiles
    manufact = models.ForeignKey(WingManufact, verbose_name="Manufacturer")
    model = models.CharField(max_length=30)
    created_at = models.DateTimeField(verbose_name="Created on", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Edited on", auto_now=True)

    def __unicode__(self):
        return "%s %s" % (self.manufact, self.model)


class Site(models.Model):
    # Sites de vol
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Fly(models.Model):
    # Vol
    number = models.IntegerField()
    date = models.DateField()
    # Durée en secondes
    duration = models.IntegerField()
    # Dénivelé en mètres
    altitude = models.IntegerField()
    # Gain en mètres
    gain = models.IntegerField()
    wing = models.ForeignKey(Wing)

    def __unicode__(self):
        return str(self.number)