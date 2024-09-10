from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
#from .models import UsuarioInternet
from .mikrotik_api import cortar_servicio, habilitar_servicio,conectar_a_mikrotik
from .mikrotik_api import Router
import socket
from librouteros import connect
from librouteros.query import Key
# Datos del router MikroTik
router = Router(host='192.168.11.80', username='admin', password='qpal1234.')

def cortar_usuario(request):
    try:
    # Cortar el servicio en MikroTik
        #cortar_servicio(router, '193.178.3.3')
       # response_data = {'status': 'success'}
       conecionapi= api = conectar_a_mikrotik(router.host,router.username,router.password)
       #print('resss con', conecionapi)
       #response_data= list(api('/ip/firewall/address-list/add', {'list': 'CORTE', 'address': '192.167.3.1'}))
       #response_data = list(api(cmd='/ip/firewall/address-list',**{'list': 'CORTE', 'address': '192.167.3.1'}))
       #direccion = api('/ip/firewall/address-list add address=192.168.13.21')
       #path = api.path('interface')
       #path.add(interface='ether1', address='172.31.31.1/24')
       
    #    addr_path = api.path('/ip/address')
    #    addr_path.add(interface='ether1', address='192.168.88.4')
    #    addresses = '192.168.88.4'
       
    #    address = Key('address')
    #    query = addr_path.select(address).where(address.In(*addresses))
    #    assert address== set(row['address'] for row in query)
       
       addr_path = api.path('/ip/firewall/address-list')
       addr_path.add(address='192.168.88.4', list='CORTE', comment='corte prueba')
       
           
       response_data={'hola':'l'}

    except Exception as e:
        
        response_data = {'status': 'error', 'message': str(e)}
    
    return JsonResponse(response_data)
    

def habilitar_usuario(request):
    try:
    # Cortar el servicio en MikroTik
        #cortar_servicio(router, '193.178.3.3')
       # response_data = {'status': 'success'}
       conecionapi= api = conectar_a_mikrotik(router.host,router.username,router.password)
       
       addr_path2 = list(api('/ip/firewall/address-list/print'))
       addr_path = api.path('/ip/firewall/address-list')
       numero_lista = 0
       print('lista:', addr_path2[0])
       
       for aaa in addr_path2:
           print(aaa['address'])
           if aaa['address'] == '192.168.88.4':
               print('SI EXISTE', numero_lista)
               addr_path.remove(str(numero_lista))
           numero_lista = numero_lista + 1
       
       
     
       addr_path = api.path('/ip/firewall/address-list')
       #addr_path.add(address='192.178.88.3', list='CORTE', comment='corte prueba')
       query = Key('address') == '192.178.88.2'
       
       print('query', query)
       
       item_to_remove = addr_path.select(query)
       

       
       if item_to_remove:
            # Eliminar la entrada usando su '.id'
            #addr_path.remove('0')
            print(f'Servicio habilitado para , eliminado de la lista CORTE')
       else:
            print(f'La IP  no se encontró en la lista CORTE.')
       

       
       
           
       response_data={'hola':'l'}

    except Exception as e:
        
        response_data = {'status': 'error', 'message': str(e)}
    
    return JsonResponse(response_data)
    




