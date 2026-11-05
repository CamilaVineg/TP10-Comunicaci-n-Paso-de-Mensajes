# Ejercicio 3 - Interfaz de comunicación confiable con sockets TCP

## Objetivo
Implementar una interfaz de comunicación confiable entre procesos usando **sockets TCP** (SOCK_STREAM).

## ¿Por qué TCP es confiable?
TCP proporciona, a nivel de transporte:
- **Orientación a conexión**: `connect()` / `accept()` establecen un canal antes de enviar datos.
- **Entrega confiable**: retransmisión ante pérdidas.
- **Orden**: los bytes llegan en el mismo orden en que se enviaron.
- **Control de flujo y congestión**: adapta el envío a la capacidad del receptor/red.

En la aplicación se usa un delimitador (`\n`) para separar mensajes, ya que TCP es un stream de bytes.

## Archivos (carpeta `Ejercicio 3`)
- `tcp_servidor.py`: servidor TCP que acepta clientes, recibe mensajes y responde con ACK.
- `tcp_cliente.py`: cliente TCP que envía un mensaje (o varios en modo interactivo) y muestra el ACK.

## Uso

### Servidor
```bash
python tcp_servidor.py 0.0.0.0 6000
```

### Cliente (mensaje único)
```bash
python tcp_cliente.py 127.0.0.1 6000 "Hola desde cliente TCP"
```

### Cliente (modo interactivo)
```bash
python tcp_cliente.py 127.0.0.1 6000 -i
```

## Prueba entre dos computadoras
1. En la máquina servidor: `python tcp_servidor.py 0.0.0.0 6000`
2. En la máquina cliente: `python tcp_cliente.py IP_DEL_SERVIDOR 6000 "mensaje"`
3. Verificar que el firewall permita TCP en el puerto elegido.

## Diferencia con el Ejercicio 1 (UDP)
| Aspecto | UDP (Ej. 1) | TCP (Ej. 3) |
|---|---|---|
| Conexión | No | Sí |
| Confiabilidad | No garantizada | Garantizada por el protocolo |
| Orden | No garantizado | Garantizado |
| Tipo de socket | `SOCK_DGRAM` | `SOCK_STREAM` |
