#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pynng
import time

ipc_address = "ipc:///tmp/abcde"
tcp_address = "tcp://127.0.0.1:4321"

with pynng.Pair0(recv_timeout=100, send_timeout=100) as sock:
    sock.dial(ipc_address)

    while True:
        try:
            # send
            sock.send(f"send to server times".encode())

            # receive
            msg = sock.recv()
            print(f"got message from server, {msg.decode()}")

        except pynng.Timeout:
            pass
        time.sleep(0.5)
