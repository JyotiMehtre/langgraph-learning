import asyncio
import random

orders = [] #file

async def C(ordertype:str, orderid:str):
    """courier organization
    """
    print("C-taking order")
    await asyncio.sleep(3)
    print("C-finished order")

async def B():
    """employee who uses courier to get items
    """
    val = random.randint(10,1000)
    order_id = f"recieveB-{val}"
    await C("receive", order_id)
    orders.append(order_id)

async def X():
    """employee who uses courier to send items
    """
    val = random.randint(1000,10000)
    order_id = f"sendX-{val}"
    await C("send", order_id)
    orders.append(order_id)

async def A():
    """supervisor
    """
    t1 = asyncio.create_task(B())
    t2 = asyncio.create_task(X())
    await t1
    await t2
    print("Completed")

if __name__ == "__main__":
    asyncio.run(A())
    for order in orders:
        print(order)
