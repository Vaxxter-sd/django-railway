from django.shortcuts import render

# Create your views here.
def render_home(request):
    return render(request, 'home.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import LeadCRM

@csrf_exempt  # Solo para pruebas; en producción usarías autenticación
@require_http_methods(["POST"])
def recibir_lead_api(request):
    try:
        data = json.loads(request.body)
        nombre = data.get('nombre')
        correo = data.get('correo')
        tipo_escuela = data.get('tipo_escuela')
        fecha_registro = data.get('fecha_registro')  # opcional, puedes usar datetime.now()

        # Crear el lead en la base de datos del CRM
        lead = LeadCRM.objects.create(
            nombre=nombre,
            correo=correo,
            tipo_escuela=tipo_escuela,
            # fecha_registro se asigna automáticamente si no la envías
        )
        return JsonResponse({'status': 'ok', 'id': lead.id}, status=201)
    except Exception as e:
        return JsonResponse({'status': 'error', 'mensaje': str(e)}, status=400)
