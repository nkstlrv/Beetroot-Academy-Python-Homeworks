import socket
import time
import multiprocessing
import concurrent.futures


HOST = '127.0.0.1'
PORT = 1234


def client_handler(connection):

    while True:
        data = connection.recv(1024)
        print(f'[DATA RECEIVED] --> {data.decode()}')
        connection.sendall(data.upper())

        if data.decode() == 'stop':
            print("Stopping server...")
            break
    connection.close()
    return False


def server_main():
    with socket.socket() as server:
        server.bind((HOST, PORT))
        server.listen()
        print('[LISTENING]')

        while True:

            connection, addr = server.accept()

            with concurrent.futures.ProcessPoolExecutor() as executor:
                p1 = executor.submit(client_handler, connection)
                res = p1.result()

            if res is False:
                break
        print('[SERVER STOPPED]')


if __name__ == "__main__":

    server_main()







