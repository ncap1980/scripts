#!/bin/python

import socket
import struct

def wake_on_lan(mac_address):
    # Comprueba que la dirección MAC es válida
    if len(mac_address) == 17 and mac_address.count(':') == 5:
        # Convierte la dirección MAC en bytes
        mac_bytes = bytes.fromhex(mac_address.replace(':', ''))
        # Crea el paquete mágico
        magic_packet = b'\xff' * 6 + mac_bytes * 16
        # Envía el paquete mágico a través de la red
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(magic_packet, ('<broadcast>', 9))
        print(f"Paquete WOL enviado a {mac_address}")
    else:
        print("Dirección MAC no válida")

# Reemplaza 'XX:XX:XX:XX:XX:XX' con la dirección MAC de tu PC
wake_on_lan('4C:ED:FB:94:9B:22')