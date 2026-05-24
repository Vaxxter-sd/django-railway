from django.contrib import admin

# Register your models here.
from .models import LeadFromFlask

@admin.register(LeadFromFlask)
class LeadFromFlaskAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'tipo_escuela', 'fecha_registro')
    list_filter = ('tipo_escuela',)
    search_fields = ('nombre', 'correo')
