import asyncio

HOST = '127.0.0.1'
PORT = 3003


async def client_func():

    reader, writer = await asyncio.open_connection(HOST, PORT)
    print('[CONNECTED]')

    while True:

        message = input('--> ')
        writer.write(message.encode())
        await writer.drain()

        received = await reader.read(1024)
        print(f"Received --> [{received.decode()}]")

        if message == 'stop':
            break

    writer.close()
    await writer.wait_closed()
    print('[CLOSED]')


if __name__ == "__main__":
    asyncio.run(client_func())