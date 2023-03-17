import socket
import caesar_cipher_algorithm

IP = '127.0.0.1'
PORT = 12345

msg = "Very secret message"

encrypted_msg = caesar_cipher_algorithm.caesar_encoder(msg, 3)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

client.sendall(encrypted_msg.encode('utf-8'))

server_return = client.recv(1024).decode('utf-8')
print(f"Server received --> {server_return}")

client.close()

