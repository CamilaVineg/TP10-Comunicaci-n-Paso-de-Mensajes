# Ejercicio 1 - Comunicación con Sockets UDP (Datagramas)

## Descripción
Implementación del ejercicio 1: utilizar la interfaz socket con servicio de datagramas para enviar y recibir mensajes de texto entre dos computadoras.

## Archivos
- `udp_servidor.py` - Servidor UDP que escucha mensajes y responde con ACK
- `udp_cliente.py` - Cliente UDP que envía mensajes al servidor

## Uso

### En la computadora que actuará como servidor
```bash
python udp_servidor.py 0.0.0.0 5000
```

### En la otra computadora (cliente)
Reemplazar `IP_DEL_SERVIDOR` con la IP de la máquina que corre el servidor:
```bash
python udp_cliente.py IP_DEL_SERVIDOR 5000 "Hola, este es un mensaje de prueba"
```

## Notas
- Asegurarse de que ambos equipos estén en la misma red o tener rutas configuradas
- Verificar que el firewall permita el tráfico UDP en el puerto utilizado
- El servidor muestra la IP y puerto del cliente que envía el mensaje
- El cliente espera una respuesta (ACK) con timeout de 5 segundos
