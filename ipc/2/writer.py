#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mmap

SIZE = 16
MMAP_FILE = "hello.txt"

# 1. create an empty file
with open(MMAP_FILE, "wb") as f:
    f.seek(SIZE - 1)
    f.write(b"\0")

# 2. use as memory mapped file
with open(MMAP_FILE, "r+b") as f:
    # memory-map the file, size 0 means whole file
    shmm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(shmm.readline())  # prints b"Hello Python!\n"
    # read content via slice notation
    print(shmm[:5])  # prints b"Hello"
    # update content using slice notation;
    # note that new content must have same size
    s = b"hello world!"
    shmm[1 : len(s) + 1] = b"hello world!"
    # ... and read again using standard file methods
    shmm.seek(0)
    print(shmm.readline())  # prints b"Hello  world!\n"

    input("Press Enter to continue...")

    # close the map
    shmm.close()
