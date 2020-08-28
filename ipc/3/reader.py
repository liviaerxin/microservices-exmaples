#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mmap

with open("hello.txt", "r+b") as f:
    shm = mmap.mmap(f.fileno(), 0)
    print(shm.readline())
    print(shm[:5])
    shm.seek(0)
    print(shm.readline())
    shm.close()