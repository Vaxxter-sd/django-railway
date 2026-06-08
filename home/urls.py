from django.urls import path
from home import views
from home.views import recibir_lead_api

urlpatterns = [
    path('', views.render_home, name='home')
    path('api/recibir-lead/', recibir_lead_api, name='recibir_lead_api'),
]
