from django.db import models

from django.db import models

class LeadFromFlask(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    tipo_escuela = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False          # No crear la tabla en la BD
        db_table = 'leads'       # Nombre exacto de la tabla en Clever Cloud
        verbose_name = 'Lead desde Flask'
        verbose_name_plural = 'Leads desde Flask'

    def __str__(self):
        return self.nombre
