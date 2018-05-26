import asyncio
import random
from asgiref.sync import sync_to_async


# async def slow_routine():
#     await asyncio.sleep(3)
#     return [random.randrange(1, 10) for _ in range(5)]
#
#
# async def sqrt_list():
#     rand_list = await slow_routine()
#     print("rand_list", rand_list)
#     result = []
#     for num in rand_list:
#         result.append(pow(num, 0.5))
#     #print(result)
#     return result
#
# loop = asyncio.get_event_loop()
# print(loop.run_until_complete(sqrt_list()))


@sync_to_async
def pow(num):
    return num*num


async def slow_routine(min, max, coun_r_num):
    await asyncio.sleep(2)
    return [random.randrange(min, max) for _ in range(coun_r_num)]


async def sqrt_list(min, max, coun_r_num):
    rand_list = await slow_routine(min, max, coun_r_num)
    print(min, max, rand_list)
    result = []
    for num in rand_list:
        result.append(await pow(num))
    print(min, max, result)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(sqrt_list(1, 10, 500), sqrt_list(11, 20, 300), sqrt_list(21, 30, 6), sqrt_list(31, 40, 3)))






