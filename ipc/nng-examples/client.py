#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pynng import Req0, Rep0
import pynng
import time
import numpy as np

ipc_address = "ipc:///tmp/abcde"
tcp_address = "tcp://127.0.0.1:4321"

with Req0(dial=ipc_address, recv_timeout=100, send_timeout=100) as req:
    # send
    message = f"send to server times"
    req.send(message.encode())

    # receive
    msg = req.recv()
    print(f"got message from server, {msg.decode()}")
