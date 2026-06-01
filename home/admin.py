from django.contrib import admin
from .models import LeadFromFlask
import csv
from django.http import HttpResponse

class LeadFromFlaskAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'tipo_escuela', 'fecha_registro', 'estado')
    list_filter = ('estado', 'tipo_escuela')
    search_fields = ('nombre', 'correo')
    list_editable = ('estado',)   # permite editar estado directamente en la lista
    actions = ['exportar_a_csv']

    def exportar_a_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="leads.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Nombre', 'Correo', 'Tipo escuela', 'Fecha registro', 'Estado', 'Notas'])
        for lead in queryset:
            writer.writerow([lead.id, lead.nombre, lead.correo, lead.tipo_escuela,
                             lead.fecha_registro.strftime('%Y-%m-%d %H:%M'), lead.estado, lead.notas])
        return response
    exportar_a_csv.short_description = "Exportar seleccionados a CSV"

admin.site.register(LeadFromFlask, LeadFromFlaskAdmin)
