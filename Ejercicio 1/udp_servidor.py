#!/usr/bin/env python3
import socket
import sys

def main():
    if len(sys.argv) < 3:
        print("Uso: python udp_servidor.py <IP_BIND> <PUERTO>")
        print("Ejemplo: python udp_servidor.py 0.0.0.0 5000")
        sys.exit(1)
    
    ip_bind = sys.argv[1]
    puerto = int(sys.argv[2])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip_bind, puerto))
    
    print(f"[SERVIDOR UDP] Escuchando en {ip_bind}:{puerto}...")
    print("Esperando mensajes. Presiona Ctrl+C para salir.")
    
    try:
        while True:
            data, addr = sock.recvfrom(4096)
            mensaje = data.decode('utf-8')
            print(f"[RECIBIDO] De {addr[0]}:{addr[1]} -> {mensaje}")
            respuesta = f"ACK: Mensaje recibido - {mensaje}"
            sock.sendto(respuesta.encode('utf-8'), addr)
            print(f"[ENVIADO] ACK a {addr[0]}:{addr[1]}")
    except KeyboardInterrupt:
        print("\n[SERVIDOR UDP] Cerrando...")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
