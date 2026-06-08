from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin
from .models import LeadCRM  # ← Cambiamos a LeadCRM

class LeadResource(resources.ModelResource):
    class Meta:
        model = LeadCRM
        fields = ('id', 'nombre', 'correo', 'tipo_escuela', 'fecha_registro', 'estado', 'notas')
        export_order = ('id', 'nombre', 'correo', 'tipo_escuela', 'fecha_registro', 'estado', 'notas')

@admin.register(LeadCRM)  # ← Registramos LeadCRM
class LeadCRMAdmin(ExportActionModelAdmin):
    resource_class = LeadResource
    list_display = ('nombre', 'correo', 'tipo_escuela', 'fecha_registro', 'estado')
    list_editable = ('estado',)        # permite cambiar estado directamente en la lista
    list_filter = ('estado', 'tipo_escuela')
    search_fields = ('nombre', 'correo')
    readonly_fields = ('fecha_registro',)
