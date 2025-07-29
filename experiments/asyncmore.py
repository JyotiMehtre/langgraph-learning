import aiohttp

import asyncio
async def get_data_from_a():
    print("Getting data from a")
    await asyncio.sleep(5)
    print("Completed reciveing data from a")


async def get_data_from_b():
    print("Getting data from b")
    await asyncio.sleep(2)
    print("Completed reciveing data from b")

async def make_http_call():

    #with statment to get http connection object
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

if __name__ == '__main__':
    asyncio.run(make_http_call())



async def main():
    task_http = asyncio.create_task(make_http_call())
    task_a = asyncio.create_task(get_data_from_a())
    task_b = asyncio.create_task(get_data_from_b())
    await task_a
    await task_b
    await task_http


async def make_http_call():
    print("executing make http call")
    #with statment to get http connection object
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

if __name__ == '__main__':
    asyncio.run(main())

