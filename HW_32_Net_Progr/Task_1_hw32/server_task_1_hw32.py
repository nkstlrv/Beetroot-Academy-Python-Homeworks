import socket

HOST = '127.0.0.1'
PORT = 1234
print('Creating User Datagram Protocol server...')

server_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Server UDP socket configured')

server_udp.bind((HOST, PORT))
print(f'Bind configured')

n = 0

while True:
    packet, address = server_udp.recvfrom(1024)
    print('Packet message: ', packet.decode('utf-8'))


