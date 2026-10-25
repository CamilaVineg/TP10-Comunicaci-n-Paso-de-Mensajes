#!/usr/bin/env python3
import socket
import sys

def main():
    if len(sys.argv) < 4:
        print("Uso: python udp_cliente.py <IP_SERVIDOR> <PUERTO_SERVIDOR> <MENSAJE>")
        print("Ejemplo: python udp_cliente.py 192.168.1.100 5000 'Hola desde cliente'")
        sys.exit(1)
    
    ip_server = sys.argv[1]
    puerto_server = int(sys.argv[2])
    mensaje = sys.argv[3]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)
    
    try:
        print(f"[CLIENTE UDP] Enviando mensaje a {ip_server}:{puerto_server}")
        sock.sendto(mensaje.encode('utf-8'), (ip_server, puerto_server))
        print(f"[ENVIADO] {mensaje}")
        
        data, addr = sock.recvfrom(4096)
        respuesta = data.decode('utf-8')
        print(f"[RECIBIDO] De {addr[0]}:{addr[1]} -> {respuesta}")
    except socket.timeout:
        print("[ERROR] Tiempo de espera agotado. No se recibió respuesta.")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
