import socket
import sys


#Dirección y puerto al cual nos vamos a comunicar
host, port = "127.0.0.1", 8888

#Generamos un nuevo socket
socket_cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Establecemos la conexión

socket_cliente.connect((host,port))

while True:
    #guardamos el mensaje del cliente
    message = input()
    if message != 'gracias':
        #enviamos mensaje al servidor
        socket_cliente.send(message.encode())
        server_response = socket_cliente.recv(4096).decode()
        print(server_response)
    else:
        socket_cliente.send(message.encode())

#cerramos el socket
print('s')
socket_cliente.close()
sys.exit()
