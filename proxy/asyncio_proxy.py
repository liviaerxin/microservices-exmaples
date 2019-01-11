#!/usr/bin/env python3.6
"""
https://docs.python.org/3.6/library/asyncio-protocol.html#protocols
https://medium.com/@pgjones/an-asyncio-socket-tutorial-5e6f3308b8b0
"""

import asyncio
import os
import datetime
import logging
import logging.config
import sys
import h11

from proxy import HttpParser

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

loop = asyncio.get_event_loop()

"""
http proxy mechanism flow:
client --[1]--> proxy --[2]--> destination server
client <--[4]-- proxy <--[3]-- destination server

[1]: data received from client(request_from_client)
[2]: data sent by proxy(request_from_proxy)
[3]: data received from destination server(response_from_destination)
[4]: data sent by proxy(response_from_proxy)

[1] = [2]
[3] = [4]

using chain of coroutines to achieve a simple and sync-like processing
prime functions in proxy:

async handle_data_from_client(reader, writer):
    data = reader.read()
    r = http_request_parse(data)
    data_from_destination = await send_data_to_destination(r.host, r.port, data)
    writer.write(data_from_destination)
    await writer.drain()

async send_data_to_destination(host, port, data):
    http_response_parse(data)

* data is byte string
"""

async def handle_data_from_client(reader, writer):
    # read client data
    conn = h11.Connection(h11.SERVER)

    event = None
    while True:
        event = conn.next_event()
        if event is h11.NEED_DATA:
            #if conn.they_are_waiting_for_100_continue:
            #    do_sendall(conn, h11.InformationalResponse(100, ...))
            data = await reader.readline() #reader.read(max_size)
            conn.receive_data(data)
            continue
        else:
            break
    
    if event is h11.Request:
        response = await send_data_to_destination()


    # write response back to client
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (response.decode(), addr))

    print("Send: %r" % response.decode())
    writer.write(response)
    await writer.drain()

    print("Close the client socket")
    writer.close()

async def send_data_to_destination(host, port, data):
    conn = h11.Connection(h11.CLIENT)
    reader, writer = await asyncio.open_connection('127.0.0.1', port)
    print('->proxy sending: %r' % data.decode())
    writer.write(data)
    await write.drain()
    conn.receive_data(data)
    response = b''
    i = 0
    while not reader.at_eof(): 
        chunk = await reader.readline()
        # if chunk == b'':
        #     break
        logger.info('read chunk: {}th with content: {}'.format(i, chunk))
        i = i + 1
        response += chunk

    print('<- Client received: %r' % response.decode())
    print('-- Terminating connection on client')
    writer.close()
    return response

class HttpProxy(asyncio.Protocol):
    def __init__(self, data):
        self.data = data
        self.start_time = self._now()
        self.request = HttpParser(HttpParser.types.REQUEST_PARSER)
        self.response = HttpParser(HttpParser.types.RESPONSE_PARSER)


    @staticmethod
    def _now():
        return datetime.datetime.utcnow()

    async def send(self):
        # parse http request
        self.request.parse(self.data)
        if self.request.state == HttpParser.states.COMPLETE:
            print('request parser is in state complete')
            # print(self.request.__dict__)
            if self.request.method == b'CONNECT':
                host, port = self.request.url.path.split(COLON)
            elif self.request.url:
                host, port = self.request.url.hostname, self.request.url.port if self.request.url.port else 80
            else:
                raise Exception('Invalid request\n%s' % self.request.raw)
            response = await tcp_echo_client(host, port, self.data)
            return response

async def start_proxy(transport, proxy):
    response = await proxy.send()
    #proxy.send()

    #response = b'aaaaaaaaaaaaaaaaaaaa'
    print('Send: {!r}'.format(response))
    transport.write(response)

    print('Close the client socket')
    transport.close()

class TcpSeverProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        proxy = HttpProxy(data)

        print('Create Proxy Task')
        loop.create_task(start_proxy(self.transport, proxy))


# create_server
coro = loop.create_server(TcpSeverProtocol, '127.0.0.1', 8888)
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