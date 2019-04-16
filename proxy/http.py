#!/usr/bin/env python3.6
"""
https://medium.com/@pgjones/an-asyncio-socket-tutorial-5e6f3308b8b0
https://docs.python.org/3.6/library/asyncio.html
https://h11.readthedocs.io/en/latest/index.html
"""

import asyncio
import h11

recv_size = 100

def text_response(message):
    """
    message is a string
    """
    # convert str to bytes
    body = str.encode(message)
    headers = [
        ('content-type', 'text/plain'),
        ('content-length', str(len(body))),
    ]
    h11_header = h11.Response(status_code=200, headers=headers)
    h11_body = h11.Data(data=body)
    return h11_header, h11_body

# handle http request from client and send response back
async def handle_http(reader, writer):
    # client info
    addr = writer.get_extra_info('peername')
    print('start to handle the request from client {}...'.format(addr))
    # parse the http request
    # read client data
    conn = h11.Connection(h11.SERVER)
    print("h11 states: {}".format(conn.states))
    request_raw = b''
    request_header = None
    request_body = None

    # 1. read the header
    # h11 event is expected to be h11.Request after proceeding
    print("reading header in the request...")
    event = None
    while True:
        data = await reader.read(recv_size) #reader.read(max_size)
        print('read chunk: {}'.format(data))
        request_raw += data
        conn.receive_data(data)
        event = conn.next_event()
        print("h11 event is {}".format(type(event)))
        if type(event) is h11.NEED_DATA:
            continue
        elif type(event) is h11.Request:
            print("the header is {}".format(event))
            request_header = event
            break
        else:
            print("server paused")
            break
    print("h11 states {}".format(conn.states))

    # 2. read the body
    # h11 event is expected to be h11.EndOfMessage or h11.DATA after proceeding
    print("reading body in the request...")
    if type(event) is h11.Request:
        event = conn.next_event()
        if type(event) is h11.EndOfMessage:
            print("the body is empty, and stop reading from reader stream")
        elif type(event) is h11.NEED_DATA:
            print("the body has content, and keep on reading from reader stream")
            while True:
                data = await reader.read(recv_size) #reader.read(max_size)
                print('read chunk: {}'.format(data))
                conn.receive_data(data)
                request_raw += data
                event = conn.next_event()
                print("h11 event is {}".format(type(event)))
                if type(event) is h11.NEED_DATA:
                    continue
                elif type(event) is h11.DATA:
                    print("the body is {}".format(event))
                    request_body = event
                    break
                else:
                    break
        else:
            print("unexpected event {}".format(event))
    print("h11 states {}".format(conn.states))

    # 3. finish the request reading
    # h11 event is expected to be h11.EndOfMessage after proceeding
    print("finishing the request reading...")
    if type(event) is h11.Data:
        event = conn.next_event()
        if event is h11.EndOfMessage:
            print("complete request reading")
            pass
        else:
            print("unexpected event {}".format(event))
    elif type(event) is h11.EndOfMessage:
        print("complete request reading")
        pass
    else:
        print("unexpected event {}".format(event))
    print("h11 states {}".format(conn.states))

    # 4. prepare the response
    print("preparing the response...")
    h11_response_header = None
    h11_response_body = None
    if type(event) is h11.EndOfMessage:
        # TODO: response = await send_data_to_destination()
        # compose a `text/plain` content type response
        message = 'received'
        h11_response_header, h11_response_body = text_response(message)
    else:
        print("unexpected event {}".format(event))
        message = 'server error'
        h11_response_header, h11_response_body = text_response(message)

    # 5. send the response to client
    print("sending the response to client {}".format(addr))
    # header
    data = conn.send(h11_response_header)
    writer.write(data)
    print("send header: {}".format(data))
    print("h11 states {}".format(conn.states))
    # body
    data = conn.send(h11_response_body)
    writer.write(data)
    print("send body: {}".format(data))
    print("h11 states {}".format(conn.states))
    # eof
    data = conn.send(h11.EndOfMessage())
    writer.write(data)
    print("send eof: {}".format(data))
    print("h11 states {}".format(conn.states))

    await writer.drain()

    # 6. close the client
    print("close the client socket")
    conn.send(h11.ConnectionClosed())
    print("h11 states {}".format(conn.states))
    writer.close()



loop = asyncio.get_event_loop()

coro = asyncio.start_server(handle_http, '127.0.0.1', 8888, loop=loop)


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
