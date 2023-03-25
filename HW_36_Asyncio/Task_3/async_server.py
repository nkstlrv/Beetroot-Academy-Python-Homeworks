import asyncio

HOST = '127.0.0.1'
PORT = 3003

run_server = True


async def client_handler(reader, writer):

    while True:

        data = await reader.read(1024)
        print(f"Received --> {data.decode()}")

        writer.write(data.upper())
        await writer.drain()

        if data.decode() == 'stop':
            global run_server
            print('Stopping server...')
            break
    writer.close()
    await writer.wait_closed()


async def server_func():

    server = await asyncio.start_server(client_handler, HOST, PORT)
    print('[RUNNING]')

    async with server:
        await server.serve_forever()

        if run_server is not True:
            asyncio.get_event_loop().stop()
            print('[CLIENT STOPPED]')


if __name__ == "__main__":

    asyncio.run(server_func())


