import socket

IP = '127.0.0.1'
PORT = 12345

server_tcp = socket.socket()
print('TCP Socket configured')

server_tcp.bind((IP, PORT))
server_tcp.listen(1)
print('Listening...')

connection, address = server_tcp.accept()
print(f"Connected to {address[0]}")

while True:

    packet = connection.recv(1024)
    print(f"Data received --> {packet.decode('utf-8')}")
    if not packet:
        break
    connection.send(packet.upper())
    print('Message was sent back')


connection.close()
print('Connection is closed')




