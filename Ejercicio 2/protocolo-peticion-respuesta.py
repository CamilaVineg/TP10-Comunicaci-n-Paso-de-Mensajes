#!/usr/bin/env python3
import socket
import sys
import time

"""Ejercicio 2: Protocolo petición-respuesta con sockets UDP.
Cada proceso envía y recibe mensajes en puertos distintos.
Modos:
  2vias: Petición -> Respuesta
  3vias: Petición -> Confirmación -> Respuesta final
  4vias: Petición -> Ack1 -> Procesamiento/Respuesta -> Ack2
"""

def main():
    if len(sys.argv) < 6:
        print("Uso: python ej2_proceso.py <rol:A|B> <ip_local> <puerto_rx> <ip_remoto> <puerto_tx> <modo:2vias|3vias|4vias> [mensaje]")
        print("Ejemplo A (inicia): python ej2_proceso.py A 0.0.0.0 5001 127.0.0.1 5002 2vias \"Hola B\"")
        print("Ejemplo B (responde): python ej2_proceso.py B 0.0.0.0 5002 127.0.0.1 5001 2vias")
        sys.exit(1)

    rol = sys.argv[1].upper()
    ip_local = sys.argv[2]
    puerto_rx = int(sys.argv[3])
    ip_remoto = sys.argv[4]
    puerto_tx = int(sys.argv[5])
    modo = sys.argv[6].lower()
    mensaje_inicial = sys.argv[7] if len(sys.argv) > 7 else "Petición de prueba"

    if modo not in ("2vias", "3vias", "4vias"):
        print("Modo inválido. Use 2vias, 3vias o 4vias.")
        sys.exit(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip_local, puerto_rx))
    sock.settimeout(10)
    remoto = (ip_remoto, puerto_tx)

    print(f"[{rol}] RX en {ip_local}:{puerto_rx} | TX a {ip_remoto}:{puerto_tx} | modo={modo}")

    try:
        if rol == "A":
            iniciar(sock, remoto, modo, mensaje_inicial)
        elif rol == "B":
            responder(sock, remoto, modo)
        else:
            print("Rol inválido. Use A o B.")
    except socket.timeout:
        print(f"[{rol}] Timeout esperando mensaje.")
    except KeyboardInterrupt:
        print(f"\n[{rol}] Interrumpido.")
    finally:
        sock.close()


def enviar(sock, remoto, texto, tag):
    sock.sendto(texto.encode("utf-8"), remoto)
    print(f"[TX] {tag}: {texto}")


def recibir(sock, tag):
    data, addr = sock.recvfrom(4096)
    texto = data.decode("utf-8")
    print(f"[RX] {tag} desde {addr[0]}:{addr[1]}: {texto}")
    return texto, addr


def iniciar(sock, remoto, modo, mensaje):
    if modo == "2vias":
        enviar(sock, remoto, f"REQ: {mensaje}", "Petición")
        recibir(sock, "Respuesta")
    elif modo == "3vias":
        enviar(sock, remoto, f"REQ: {mensaje}", "Petición")
        recibir(sock, "Confirmación")
        enviar(sock, remoto, "ACK_FINAL: listo para recibir respuesta", "ACK final")
        recibir(sock, "Respuesta final")
    elif modo == "4vias":
        enviar(sock, remoto, f"REQ: {mensaje}", "Petición")
        recibir(sock, "ACK1")
        recibir(sock, "Respuesta")
        enviar(sock, remoto, "ACK2: respuesta recibida", "ACK2")


def responder(sock, remoto, modo):
    print("[B] Esperando petición...")
    if modo == "2vias":
        req, _ = recibir(sock, "Petición")
        time.sleep(0.2)
        enviar(sock, remoto, f"RESP: procesado -> {req}", "Respuesta")
    elif modo == "3vias":
        req, _ = recibir(sock, "Petición")
        enviar(sock, remoto, "CONF: petición recibida, procesando", "Confirmación")
        recibir(sock, "ACK final")
        time.sleep(0.2)
        enviar(sock, remoto, f"RESP_FINAL: procesado -> {req}", "Respuesta final")
    elif modo == "4vias":
        req, _ = recibir(sock, "Petición")
        enviar(sock, remoto, "ACK1: petición recibida", "ACK1")
        time.sleep(0.2)
        enviar(sock, remoto, f"RESP: procesado -> {req}", "Respuesta")
        recibir(sock, "ACK2")


if __name__ == "__main__":
    main()
