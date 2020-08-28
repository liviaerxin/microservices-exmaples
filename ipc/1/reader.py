#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sysv_ipc as ipc


def main():
    path = "./"
    key = ipc.ftok(path, 2333)
    shm = ipc.SharedMemory(key, 0, 0)

    # I found if we do not attach ourselves
    # it will attach as ReadOnly.
    shm.attach(0, 0)
    buf = shm.read(
        0, 0
    )  # If byte_count is zero (the default) the entire buffer is returned.
    print(buf)
    shm.detach()
    pass


if __name__ == "__main__":
    main()
