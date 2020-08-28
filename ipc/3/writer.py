#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mmap

# 1. create a simple example file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

# 2. open as mmap
with open("hello.txt", "r+b") as f:
    shm = mmap.mmap(
        f.fileno(), 0
    )  # You should "open" the memory map file instead of attempting to create it..

    if shm:
        print(f"previous: {shm.readline()}")

        shm.seek(0)
        shm.write(bytes("5", "UTF-8"))
        shm.write(bytes("Hello", "UTF-8"))

        shm.seek(0)
        print(f"after: {shm.readline()}")
        print("GOOD")

        input("Press Enter to exit...")

        shm.close()
