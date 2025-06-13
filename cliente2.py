#CLIENTE

import socket
import sys

mi_socket=socket.socket()
mi_socket.bind(("10.120.3.135",12346))
mi_socket.connect(('10.120.3.135',12345))#ip y puerto el cual servidor o cliente se va conectar
usuario=input("usuario")
contraseña=input("contraseña")
mi_socket.send(usuario.encode())
mi_socket.send(contraseña.encode())
respuesta=mi_socket.recv(1024)


print("servidor dice", respuesta.decode())
print("servidor dice", respuesta.decode())
mi_socket.close()