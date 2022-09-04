import socket
from urllib import request

#Dirección y puerto al cual nos vamos a comunicar
host, port = "127.0.0.1", 8888

#Generamos un nuevo socket
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Establecemos la conexión

socket_server.bind((host,port))
socket_server.listen()

while True:
    #Establecemos la conexión 
    connection, address = socket_server.accept()
    print("Cliente conecado:",address)
    #Inter acción entre cliente o mensaje del cliente
    while True: 
        #Solicitud del cliente o mensaje del cliente
        customer_message = connection.recv(4096).decode()
        print(customer_message)

        if customer_message == 'gracias':
            break

        #Enviamos respuesta al cliente
        connection.send(input().encode())

print("Cliente desconectado")
connection.close()

