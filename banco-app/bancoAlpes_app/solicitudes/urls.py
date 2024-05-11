from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('solicitudes/', views.solicitud_list, name='solicitudesList'),
    path('solicitudescreate/', csrf_exempt(views.solicitud_create), name='solicitudesCreate'),
    path('solicitudesupdate/<int:solicitud_id>', csrf_exempt(views.solicitud_update), name='solicitudesUpdate')
]