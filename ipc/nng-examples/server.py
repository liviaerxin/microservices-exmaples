#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import numpy as np
import pynng
import argparse
import os

ipc_address = "ipc:///tmp/abcde"
tcp_address = "tcp://127.0.0.1:4321"


def serve(address, np_convert):
    with pynng.Rep0(listen=address, recv_timeout=100, send_timeout=100) as rep:

        while True:
            try:
                # receive
                msg = rep.recv()
                # print(f"got message from client, {msg.decode()}")
                # print(f"total received byte size, {len(msg)}")
                if np_convert:
                    input = np.frombuffer(msg, dtype=np.uint8)
                    print(input.shape)
                # output
                output = np.zeros((1024), dtype=np.uint8).tobytes()

                # send
                rep.send(output)

            except pynng.Timeout:
                pass
            except KeyboardInterrupt:
                break
            except Exception:
                break
            # time.sleep(0.0001)


def main():
    # Parse Argument
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--address", help="ipc/tcp/ws address", default="ipc:///tmp/abcde", type=str
    )
    parser.add_argument(
        "--np_convert",
        help="whether convert input to np.array",
        default="True",
        type=eval,
        choices=[True, False],
    )

    args = parser.parse_args()

    # Start server
    serve(args.address, args.np_convert)


if __name__ == "__main__":
    main()
