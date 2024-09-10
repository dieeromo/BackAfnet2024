from librouteros import connect
from librouteros.query import Key

class Router:
    """
    Clase para representar un router MikroTik.
    """
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

def conectar_a_mikrotik(host, username, password):
    """
    Conectar al router MikroTik usando la API.
    """
    return connect(username=username, password=password, host=host)

def cortar_servicio(router, ip_address):
    try:
        api = conectar_a_mikrotik(router.host, router.username, router.password)
        # Agregar la dirección IP a la lista 'CORTE'
        api('/ip/firewall/address-list/add', {'list': 'CORTE', 'address': ip_address})
        
        print(f'Servicio cortado para {ip_address}')
    except Exception as e:
        print(f'Error cortando servicio para {ip_address}: {e}')
        
        

def habilitar_servicio(router, ip_address):
    """
    Elimina la IP del usuario de la address-list 'CORTE' en el router MikroTik.
    """
    try:
        api = conectar_a_mikrotik(router.host, router.username, router.password)
        # Consultar si la dirección IP está en la lista 'CORTE'
        query = Key('address') == ip_address
        lista_corte = api.path('/ip/firewall/address-list')
        address_to_remove = lista_corte.select(query).first()
        
        if address_to_remove:
            # Eliminar la dirección IP de la lista 'CORTE'
            lista_corte.remove(address_to_remove['.id'])
            print(f'Servicio habilitado para {ip_address}')
        else:
            print(f'La IP {ip_address} no está en la lista CORTE.')
    except Exception as e:
        print(f'Error habilitando servicio para {ip_address}: {e}')
