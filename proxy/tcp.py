#!/usr/bin/env python3.6

import asyncio

async def handle_echo(reader, writer):
    while True:
        data = await reader.read(100)
        addr = writer.get_extra_info('peername')
        print("Received {} bytes: {} from {}".format(len(data), data, addr))
        # only when client close the connection, EOF would be received
        # It's a pure tcp protocol, which literaly is stream object. So we do not know the
        # EOF untill client send that. In comparison to http protocol, it could recognize the
        # `ending` with help of the declared attribute `content-length` in headers, or if now 
        # content length, it maybe put an end to the stream reader by reading a b'\r\n\r\n'
        # le
        if reader.at_eof():
            break
    response = b"received"
    print("Send: {}".format(response))
    writer.write(response)
    await writer.drain()

    print("Close the client socket")
    writer.close()




class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()

loop = asyncio.get_event_loop()

# create_server
#coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)

# or start_server
coro = asyncio.start_server(handle_echo, '127.0.0.1', 8888, loop=loop)


server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()