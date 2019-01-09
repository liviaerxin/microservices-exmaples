#!/usr/bin/env python3.6

import asyncio

async def hello_world():
    await asyncio.sleep(1)
    print('Hello World')
    await good_evening()


async def good_evening():
    await asyncio.sleep(1)
    print('Good Evening')
    await hello_world()

async def create_server(loop = None):
    print('create Server')
    _start_serving(loop)
    await asyncio.sleep(1)

def _start_serving(loop = None):
    #await asyncio.sleep(10)
    print('Start Serving')
    # asyncio.async(hello_world()) and loop.create_task(hello_world()) both attach a coroutine into the loop
    # in next round.
    loop.create_task(hello_world())

loop = asyncio.get_event_loop()

def test1():
    loop.run_until_complete(hello_world())
    loop.run_until_complete(good_evening())

def test2():
    asyncio.async(hello_world())
    asyncio.async(good_evening())
    loop.run_forever()

try:
    #1. Never complete the coroutine
    # test1()
    #2. Or schedule the coroutine to run in next loop
    # test2()
    #3. Create server
    server = loop.run_until_complete(create_server(loop = loop))
    loop.run_forever()
finally:
    print('closing event loop')
    loop.close()