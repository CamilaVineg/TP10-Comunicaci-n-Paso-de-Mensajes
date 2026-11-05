#!/usr/bin/env python3
"""Ejercicio 3: Interfaz de comunicación confiable con sockets TCP.
Cliente: se conecta al servidor, envía mensajes de texto y recibe ACK.
"""

import socket
import sys


def recibir_mensaje(sock):
    datos = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            return None
        datos += chunk
        if b"\n" in datos:
            linea, _, _ = datos.partition(b"\n")
            return linea.decode("utf-8", errors="replace")


def enviar_mensaje(sock, texto):
    sock.sendall((texto + "\n").encode("utf-8"))


def main():
    if len(sys.argv) < 4:
        print("Uso: python tcp_cliente.py <IP_SERVIDOR> <PUERTO> <MENSAJE>")
        print("       python tcp_cliente.py <IP_SERVIDOR> <PUERTO> -i   (modo interactivo)")
        print("Ejemplo: python tcp_cliente.py 127.0.0.1 6000 \"Hola TCP\"")
        sys.exit(1)

    ip_server = sys.argv[1]
    puerto = int(sys.argv[2])
    arg3 = sys.argv[3]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(10)
        print(f"[CLIENTE TCP] Conectando a {ip_server}:{puerto}...")
        sock.connect((ip_server, puerto))
        print("[CLIENTE TCP] Conexión establecida (canal confiable).")

        if arg3 == "-i":
            print("Modo interactivo. Escribí mensajes (vacío o Ctrl+C para salir).")
            try:
                while True:
                    msg = input("> ").strip()
                    if not msg:
                        break
                    enviar_mensaje(sock, msg)
                    resp = recibir_mensaje(sock)
                    if resp is None:
                        print("[CLIENTE TCP] Servidor cerró la conexión.")
                        break
                    print(f"[RECIBIDO] {resp}")
            except (KeyboardInterrupt, EOFError):
                print("\n[CLIENTE TCP] Saliendo...")
        else:
            enviar_mensaje(sock, arg3)
            print(f"[ENVIADO] {arg3}")
            resp = recibir_mensaje(sock)
            if resp is None:
                print("[ERROR] No se recibió respuesta (conexión cerrada).")
            else:
                print(f"[RECIBIDO] {resp}")


if __name__ == "__main__":
    main()
