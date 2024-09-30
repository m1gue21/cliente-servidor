import socket
import threading
import os

# Lista para almacenar el historial del chat en el cliente
historial_chat = []

# Función para recibir mensajes del servidor
def recibir_mensajes(cliente_socket):
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            historial_chat.append(mensaje)
            mostrar_chat()
        except:
            print("Conexión perdida.")
            cliente_socket.close()
            break

# Función para mostrar el chat limpio en pantalla
def mostrar_chat():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
    for mensaje in historial_chat:
        print(mensaje)  # Mostrar todos los mensajes del historial
    print("\nEscribir mensaje: ", end="")  # Dejar listo para el input

# Función para iniciar el cliente
def iniciar_cliente():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('localhost', 8080))

    # Solicitar nombre del cliente
    nombre_cliente = input("Por favor, ingrese su nombre: ")
    cliente_socket.send(nombre_cliente.encode('utf-8'))

    # Hilo para recibir mensajes
    hilo = threading.Thread(target=recibir_mensajes, args=(cliente_socket,))
    hilo.start()

    while True:
        mensaje = input("Escribir mensaje: ")
        cliente_socket.send(mensaje.encode('utf-8'))  # Enviar mensaje al servidor

if __name__ == "__main__":
    iniciar_cliente()
