# Chat Cliente-Servidor en Python

Este proyecto implementa un sistema de chat básico utilizando la arquitectura cliente-servidor en Python. Permite que múltiples clientes se conecten a un servidor central, enviando y recibiendo mensajes en tiempo real. La comunicación se gestiona a través de sockets TCP/IP y se utiliza concurrencia con hilos para manejar múltiples clientes simultáneamente.

## Características

- **Conexiones múltiples**: Varios clientes pueden conectarse al servidor simultáneamente.
- **Historial de mensajes**: Los mensajes se muestran de manera continua en la consola del cliente.
- **Formato de mensajes**: Los mensajes incluyen la hora de envío y el nombre del remitente.

## Tecnologías Utilizadas

- **Python**: Para manejar la concurrencia y los sockets.
- **Socket**: Protocolo de comunicación TCP/IP.
- **Threading**: Permite manejar múltiples conexiones de cliente de manera concurrente.

## Cómo Ejecutar

### Clonar el repositorio

```bash
git clone https://github.com/m1gue21/cliente-servidor.git
cd cliente-servidor
```

### Ejecutar el servidor y tantos clisntes como se desee

```bash
python server.py
python client.py
Por favor, ingrese su nombre: "nombre que desea ser usado para enviar mensajes"
```
