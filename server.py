import socket
import threading
import pymysql

miConexion= pymysql.connect(host='localhost'
                            ,user='root'
                            ,passwd=''
                            ,db='chat26')

Query=miConexion.cursor()
Consulta=Query.execute('select * from usuarios')
for fila in Query.fetchall():
 print(fila)



clave = {
    "Juan": "1234",
    "Ana": "4321"
}

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

def handle_client(conn, addr):
    print(f"Conexión establecida con {addr}")
    try:
        
        usuario = conn.recv(1024).decode().strip()
        print(f"Usuario recibido: {usuario}")

        
        contraseña = conn.recv(1024).decode().strip()
        print(f"Contraseña recibida: {contraseña}")

        if usuario in clave and clave[usuario] == contraseña:
            conn.send("Login correcto".encode())

            while True:
                # Recibir mensaje del cliente
                data = conn.recv(1024).decode().strip()
                if not data or data.lower() == "exit":
                    print(f"Cliente {addr} ha terminado la conexión.")
                    break
                print(f"Mensaje recibido de {usuario}: {data}")

               
                respuesta = f"Servidor recibió: {data}"
                conn.send(respuesta.encode())

        else:
            conn.send("Usuario o contraseña incorrecta".encode())
    except Exception as e:
        print(f"Error con el cliente {addr}: {e}")
    finally:
        conn.close()
        print(f"Conexión cerrada con {addr}")

def start_server():
    print("Tu computadora es:", hostname)
    print("Dirección IP:", ip)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, 12345))
    server_socket.listen(5)
    print("Servidor escuchando en", ip)

    while True:
        cliente_socket, addr = server_socket.accept()
        cliente_thread = threading.Thread(target=handle_client, args=(cliente_socket, addr))
        cliente_thread.start()


start_server()
