import socket

HOST = '127.0.0.1'
PORT = 1234


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client UDP socket configured')

message_to_send = input('Print the message: ')

client.sendto(message_to_send.encode('utf-8'), (HOST, PORT))