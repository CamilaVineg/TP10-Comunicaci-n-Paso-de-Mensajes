# Ejercicio 2 - Protocolo petición-respuesta con sockets UDP

## Descripción
Implementación de protocolos petición-respuesta entre dos procesos usando sockets UDP. Cada proceso envía y recibe mensajes en **puertos distintos**.

## Modos implementados
- **2 vías**: Petición -> Respuesta
- **3 vías**: Petición -> Confirmación -> ACK final -> Respuesta final
- **4 vías**: Petición -> ACK1 -> Respuesta -> ACK2

## Archivo
- `ej2_proceso.py`: programa único que puede ejecutarse como proceso A (inicia) o B (responde).

## Uso
```bash
python ej2_proceso.py <rol:A|B> <ip_local> <puerto_rx> <ip_remoto> <puerto_tx> <modo:2vias|3vias|4vias> [mensaje]
```

### Ejemplos (en la misma máquina, localhost)

#### 2 vías
Terminal 1 (Proceso B):
```bash
python ej2_proceso.py B 0.0.0.0 5002 127.0.0.1 5001 2vias
```
Terminal 2 (Proceso A):
```bash
python ej2_proceso.py A 0.0.0.0 5001 127.0.0.1 5002 2vias "Hola desde A"
```

#### 3 vías
Terminal 1 (B):
```bash
python ej2_proceso.py B 0.0.0.0 5002 127.0.0.1 5001 3vias
```
Terminal 2 (A):
```bash
python ej2_proceso.py A 0.0.0.0 5001 127.0.0.1 5002 3vias "Solicitud 3 vias"
```

#### 4 vías
Terminal 1 (B):
```bash
python ej2_proceso.py B 0.0.0.0 5002 127.0.0.1 5001 4vias
```
Terminal 2 (A):
```bash
python ej2_proceso.py A 0.0.0.0 5001 127.0.0.1 5002 4vias "Solicitud 4 vias"
```

## Entre dos computadoras
- Reemplazar `127.0.0.1` por la IP del equipo remoto correspondiente.
- Usar `0.0.0.0` o la IP local para enlazar el puerto de recepción.
- Verificar conectividad y reglas de firewall para los puertos UDP usados.

## Nota
El ejercicio usa UDP (datagramas) y un timeout básico (10s) para simplificar la demostración del protocolo petición-respuesta.