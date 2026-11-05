#!/usr/bin/env python3
"""Ejercicio 3: Interfaz de comunicación confiable con sockets TCP.
Servidor: acepta conexiones, recibe mensajes de texto y responde con ACK.
TCP provee confiabilidad (entrega ordenada, retransmisión, control de flujo/congestión).
"""

import socket
import sys


def recibir_mensaje(conn):
    """Lee un mensaje terminado en newline para delimitar mensajes en TCP."""
    datos = b""
    while True:
        chunk = conn.recv(4096)
        if not chunk:
            return None
        datos += chunk
        if b"\n" in datos:
            linea, _, resto = datos.partition(b"\n")
            # Nota: resto se ignora en este ejemplo simple (un mensaje por turno)
            return linea.decode("utf-8", errors="replace")


def enviar_mensaje(conn, texto):
    conn.sendall((texto + "\n").encode("utf-8"))


def main():
    if len(sys.argv) < 3:
        print("Uso: python tcp_servidor.py <IP_BIND> <PUERTO>")
        print("Ejemplo: python tcp_servidor.py 0.0.0.0 6000")
        sys.exit(1)

    ip_bind = sys.argv[1]
    puerto = int(sys.argv[2])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((ip_bind, puerto))
        srv.listen(5)
        print(f"[SERVIDOR TCP] Escuchando en {ip_bind}:{puerto} (confiable, orientado a conexión)")
        print("Presiona Ctrl+C para salir.")

        try:
            while True:
                conn, addr = srv.accept()
                with conn:
                    print(f"[CONEXIÓN] Cliente conectado: {addr[0]}:{addr[1]}")
                    while True:
                        msg = recibir_mensaje(conn)
                        if msg is None:
                            print(f"[CONEXIÓN] Cliente desconectado: {addr[0]}:{addr[1]}")
                            break
                        print(f"[RECIBIDO] {addr[0]}:{addr[1]} -> {msg}")
                        ack = f"ACK: mensaje recibido correctamente -> {msg}"
                        enviar_mensaje(conn, ack)
                        print(f"[ENVIADO] ACK a {addr[0]}:{addr[1]}")
        except KeyboardInterrupt:
            print("\n[SERVIDOR TCP] Cerrando...")


if __name__ == "__main__":
    main()
