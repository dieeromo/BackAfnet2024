

# Create your views here.
from rest_framework import viewsets, routers
from rest_framework.response import Response
from rest_framework.decorators import action

from librouteros import connect
from django.http import JsonResponse


def conectar_mikrotik(request):
    try:
        # Datos de conexión
        host = '192.168.11.80'
        username = 'admin'
        password = 'qpal1234.'
        
        # Conectar a MikroTik
        api = connect(username=username, password=password, host=host)
        
        # Realizar una consulta simple, por ejemplo, obtener la lista de interfaces

        interfaces = list( api('/ip/route/print'))
        response_data = {'status': 'success', 'interfaces': interfaces}
 
        
    except Exception as e:
        response_data = {'status': 'error', 'message': str(e)}
    
    return JsonResponse(response_data)

def firewall_cortar(request):
    try:
        # Datos de conexión
        host = '192.168.11.80'
        username = 'admin'
        password = 'qpal1234.'
        
        # Conectar a MikroTik
        api = connect(username=username, password=password, host=host)
        
        # Realizar una consulta simple, por ejemplo, obtener la lista de interfaces

        interfaces = list( api('/ip/firewall/address-list/add address=192.168.13.31 comment="AIDA OLIVA JARRIN MESA - 2023-04-20" list=\ CORTE'))
        response_data = {'status': 'success', 'interfaces': interfaces}
 
        
    except Exception as e:
        response_data = {'status': 'error', 'message': str(e)}
    
    return JsonResponse(response_data)
