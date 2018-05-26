import asyncio
from datetime import datetime


async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))


async def times_print():
    for i in range(10):
        print(datetime.now())
        await asyncio.sleep(0.5)

loop = asyncio.get_event_loop()
routines = [factorial("A", 2), factorial("B", 3), factorial("C", 4), times_print()]
loop.run_until_complete(asyncio.gather(*routines))

# loop.run_until_complete(asyncio.gather(
#     factorial("A", 2),
#     factorial("B", 3),
#     factorial("C", 4),
# ))

loop.close()
