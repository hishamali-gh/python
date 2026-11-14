import asyncio

import time

''' def download():
    print('Downloading...')

    time.sleep(2)

    print('Done')

download()
print('Next task')

async def hello(): # This is a Coroutine
    print('Hello')

print()

print(download)
print(hello)
print(hello())
print()

asyncio.run(hello()) '''

async def work():
    print('Start')

    await asyncio.sleep(2)

    print('Done')

async def main():
    await asyncio.gather(
        work(),
        work(),
        work()
    )

asyncio.run(main())
