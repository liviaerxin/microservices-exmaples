#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pynng
import time
import numpy as np

ipc_address = "ipc:///tmp/abcde"
tcp_address = "tcp://127.0.0.1:4321"

with pynng.Pair0(recv_timeout=100, send_timeout=100) as sock:
    sock.listen(ipc_address)

    while True:
        try:
            # receive
            msg = sock.recv()
            print(f"got message from client, {msg.decode()}")
            print(f"total received byte size, {len(msg)}")

            # send
            output = np.zeros((1024), dtype=np.uint8).tobytes()
            sock.send(output)

        except pynng.Timeout:
            pass
        time.sleep(0.5)
