# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Imagen(models.Model):
    """
    Modelo de la imagen digital que se sube al servidor.
    """
    titulo = models.CharField(max_length=255, blank=False, null=False)
    autor = models.CharField(max_length=255, blank=False, null=False)
    imagen = models.FileField(upload_to='', blank=False, null=False)
    tag = models.CharField(max_length=255, blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('registro:editar_imagen', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.titulo
