import socket
import threading
from datetime import datetime

# Diccionario para almacenar los clientes conectados y sus nombres
clientes = {}

# Función para transmitir el mensaje a todos los clientes excepto al remitente
def transmitir_mensaje(mensaje, remitente):
    for cliente_socket in clientes:
        if cliente_socket != remitente:
            try:
                cliente_socket.send(mensaje.encode('utf-8'))
            except:
                cliente_socket.close()
                del clientes[cliente_socket]

# Función para manejar a cada cliente
def manejar_cliente(cliente_socket):
    cliente_socket.send("Por favor, ingrese su nombre: ".encode('utf-8'))
    nombre_cliente = cliente_socket.recv(1024).decode('utf-8')

    # Guardar el cliente y su nombre
    clientes[cliente_socket] = nombre_cliente
    transmitir_mensaje(f"*** {nombre_cliente} ha entrado al chat ***", cliente_socket)
    print(f"{nombre_cliente} ha entrado al chat.")

    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            hora_actual = datetime.now().strftime('%H:%M:%S')
            mensaje_con_hora = f"[{hora_actual}] {nombre_cliente}: {mensaje}"
            
            # Mostrar el mensaje en el servidor
            print(mensaje_con_hora)

            # Retransmitir a todos los demás clientes
            transmitir_mensaje(mensaje_con_hora, cliente_socket)

            # Enviar de vuelta al remitente con "Tú:"
            cliente_socket.send(f"[{hora_actual}] Tú: {mensaje}".encode('utf-8'))
        except:
            cliente_socket.close()
            transmitir_mensaje(f"*** {nombre_cliente} ha salido del chat ***", cliente_socket)
            print(f"{nombre_cliente} ha salido del chat.")
            del clientes[cliente_socket]
            break

# Función para iniciar el servidor
def iniciar_servidor():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('localhost', 8080))
    servidor_socket.listen(5)
    print("Servidor en ejecución en el puerto 8080...")

    while True:
        cliente_socket, direccion = servidor_socket.accept()
        print(f"Conexión establecida con {direccion}")
        hilo = threading.Thread(target=manejar_cliente, args=(cliente_socket,))
        hilo.start()

if __name__ == "__main__":
    iniciar_servidor()
