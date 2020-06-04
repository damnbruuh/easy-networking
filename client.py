import socket

client_socket = socket.socket()

host = socket.gethostname()

port = 12345

client_socket.connect((host, port))

file_path = 'example.txt'

flag = True

client_socket.settimeout(2)

with open(file_path, 'wb') as file:

    while flag == True:

        print('Receiving data...')

        try:

            data = client_socket.recv(1024)

        except:

            print('File transmission has finished. ')

            flag = False

        file.write(data)

        print('Wrote data')

client_socket.close()
