import socket
import threading

HOST = 'localhost'
PORT = 8000

data = True


def data_receiver(client_socket):
    while True:
        global data
        data = client_socket.recv(1024)
        print(f"Data received [{data.decode()}]\n")
        client_socket.sendall(data.upper())

        if not data:
            print("No receiving data")
            print("Stopping server...")
            break

    client_socket.close()


def server_main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print('[LISTENING]')

        while data:
            client_socket, address = server.accept()
            print(f"Accepted {address}")

            t = threading.Thread(target=data_receiver, args=(client_socket,))
            t.start()
            t.join()

        print("\n[SERVER STOPPED]")


if __name__ == "__main__":
    server_main()



