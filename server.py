import socket

import threading

flag = True

def clientConnect(conn, addr):

    print('A client has connected from: ', addr)

    file_path = 'example.txt'

    with open(file_path, 'rb') as file:

        read = file.read(1024)

        while (read):

            conn.sendall(read)

            print('Sent a volume of data to: ', addr)

            read = file.read(1024)

def closeServer(socket):

    user_input = input('Enter quit to terminate server. Be aware that closing this application without entering quit will result in socket problems.')

    user_input = user_input.lower()

    if user_input == 'quit':

        socket.close()

    # handle as separate thread

server_socket = socket.socket()

host = socket.gethostname()

port = 12345

server_socket.bind((host, port))

print('Success, listening.')

server_socket.listen(5)

while flag == True:

    connection, address = server_socket.accept()

    print('Discovered connection from client socket.')

    server_thread = threading.Thread(target=clientConnect, args=(connection, address))

    server_thread.start()

    input_thread = threading.Thread(target=closeServer, args=(server_socket,))

    input_thread.start()










