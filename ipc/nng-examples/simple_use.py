#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pynng import Pair0

s1 = Pair0()
s1.listen("tcp://127.0.0.1:54321")
s2 = Pair0()
s2.dial("tcp://127.0.0.1:54321")

s1.send(b"Well hello there from s1")
print(s2.recv())
s2.send(b"Well hello there from s2")
print(s1.recv())

s1.close()
s2.close()
