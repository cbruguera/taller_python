# -*- coding: utf-8 -*-

from django.db import models


class AcademicBookManager(models.Manager):
    
    def get_queryset(self):
        return super(AcademicBookManager, self).get_queryset().filter(genero=4)


class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Autores"

    def __unicode__(self):
        return self.nombre
    

class Libro(models.Model):
    
    objects = models.Manager()
    academic = AcademicBookManager()
    
    GENERO_CHOICES = (
        (1, 'Narración'),
        (2, 'Crónica'),
        (3, 'Ensayo'),
        (4, 'Académico'),
        (5, 'Biografía'),
    )
    
    titulo = models.CharField(max_length=200)
    fecha_pub = models.DateField()
    autor = models.ForeignKey(Autor)
    genero = models.IntegerField(choices=GENERO_CHOICES, default=1)
    
    def __unicode__(self):
        return "%s - %s" % (self.titulo, self.autor.nombre)