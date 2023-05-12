import socket
import threading

HOST = 'localhost'
PORT = 8000


def client_main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        while True:
            message = input('--> ')
            client.sendall(message.encode())

            received = client.recv(1024)
            print(f"Received [{received.decode()}]")

            if message == 'stop':
                print('Client stopped')
                break


if __name__ == "__main__":
    client_main()
