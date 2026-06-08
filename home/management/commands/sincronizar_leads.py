from django.core.management.base import BaseCommand
from home.models import LeadCaptura, LeadCRM

class Command(BaseCommand):
    help = 'Sincroniza leads desde Clever Cloud (captura) a la base de datos del CRM'

    def handle(self, *args, **options):
        leads_captura = LeadCaptura.objects.using('captura').all()
        nuevos = 0
        actualizados = 0
        for lead in leads_captura:
            obj, created = LeadCRM.objects.update_or_create(
                id=lead.id,
                defaults={
                    'nombre': lead.nombre,
                    'correo': lead.correo,
                    'tipo_escuela': lead.tipo_escuela,
                    'fecha_registro': lead.fecha_registro,
                    'estado': lead.estado or 'Nuevo',
                    'notas': lead.notas or ''
                }
            )
            if created:
                nuevos += 1
            else:
                actualizados += 1
        self.stdout.write(self.style.SUCCESS(f'Sincronización completada: {nuevos} nuevos, {actualizados} actualizados.'))
