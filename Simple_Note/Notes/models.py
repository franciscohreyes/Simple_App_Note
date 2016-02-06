from django.db import models


class Cat_estatus(models.Model):
	nombre = models.CharField(max_length=80)
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s' % self.nombre

	class Meta:
		verbose_name = "Estatu"
		verbose_name_plural = "Estatus"


class Cat_notas(models.Model):
	titulo = models.CharField(verbose_name="Titulo", max_length=100, null=True, blank=True)
	descripcion = models.CharField(verbose_name="Descripción", max_length=200, null=True, blank=True)
	slug = models.SlugField(max_length=200, null=True, blank=True)
	cat_estatus = models.ForeignKey(Cat_estatus)
	fecha_creacion = models.DateField(verbose_name="Fecha", auto_now_add=True, null=True, blank=True)
	fecha_edicion = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s - %s' % (self.titulo, self.fecha_creacion)

	class Meta:
		verbose_name = "Nota"
		verbose_name_plural = "Notas"
