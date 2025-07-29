#coroutine
import asyncio
async def get_data_from_a():
    print("Getting data from a")
    await asyncio.sleep(5)
    print("Completed reciveing data from a")


async def get_data_from_b():
    print("Getting data from b")
    await asyncio.sleep(2)
    print("Completed reciveing data from b")

async def main():
    #await asyncio.gather(get_data_from_a(), get_data_from_b())
    task_a = asyncio.create_task(get_data_from_a())
    task_b = asyncio.create_task(get_data_from_b())
    await task_a
    await task_b


asyncio.run(main())