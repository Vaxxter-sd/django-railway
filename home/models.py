from django.db import models

class LeadFromFlask(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    tipo_escuela = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Nuevo')   # ← nuevo
    notas = models.TextField(blank=True, null=True)              # ← opcional

    class Meta:
        managed = False
        db_table = 'leads'
        verbose_name = 'Lead desde Flask'
        verbose_name_plural = 'Leads desde Flask'

# ==============================================
# Modelo para leer desde Clever Cloud (Base de datos de CAPTURA)
# ==============================================
class LeadCaptura(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    tipo_escuela = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField()
    estado = models.CharField(max_length=20, blank=True, null=True)
    notas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False          # Django no crea ni modifica esta tabla
        db_table = 'leads'       # Nombre exacto en la base de datos Clever Cloud
        app_label = 'home'

    def __str__(self):
        return self.nombre

# ==============================================
# Modelo para la base de datos del CRM (SQLite)
# ==============================================
class LeadCRM(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    tipo_escuela = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Nuevo')
    notas = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'leads_crm'
        verbose_name = 'Lead desde CRM'
        verbose_name_plural = 'Leads desde CRM'

    def __str__(self):
        return self.nombre
