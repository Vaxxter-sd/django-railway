from django.db import models

class LeadFromFlask(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    tipo_escuela = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Nuevo')
    notas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads'
        verbose_name = 'Lead desde Flask'
        verbose_name_plural = 'Leads desde Flask'

    def __str__(self):
        return self.nombre
