import socket
import time
from concurrent.futures import ProcessPoolExecutor

HOST = '127.0.0.1'
PORT = 1234


def client_main():
    client = socket.socket()
    client.connect((HOST, PORT))
    print('[CONNECTED]')

    while True:
        message = input("--> ")
        client.sendall(message.encode())
        rec = client.recv(1024)
        print(f"Received [{rec.decode()}]")

        if message == 'stop':
            break
    print('[DISCONNECTED}')


if __name__ == "__main__":

    client_main()
