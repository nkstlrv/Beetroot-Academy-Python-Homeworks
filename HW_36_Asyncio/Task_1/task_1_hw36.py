import asyncio


async def fibonacci_func(n):
    if n <= 1:
        return n
    else:
        return await fibonacci_func(n-1) + await fibonacci_func(n-2)


async def factorial_func(n):
    if n == 0:
        return 1
    else:
        return n * await factorial_func(n-1)


async def square_func(n):
    return n**2


async def cube_func(n):
    return n**3


async def main_func():

    coroutines = []

    fibs = []
    facts = []
    squares = []
    cubes = []

    for _ in range(1, 11):
        coroutines.append(asyncio.create_task(fibonacci_func(_)))
        coroutines.append(asyncio.create_task(factorial_func(_)))
        coroutines.append(asyncio.create_task(square_func(_)))
        coroutines.append(asyncio.create_task(cube_func(_)))

        results = await asyncio.gather(*coroutines)

    for c in range(0, 40, 4):

        fibs.append(results[c])
        facts.append(results[c+1])
        squares.append(results[c+2])
        cubes.append(results[c+3])

    print(f"Fibonacci --> {fibs}")
    print(f"Factorials --> {facts}")
    print(f"Squares --> {squares}")
    print(f"Cubes --> {cubes}")


asyncio.run(main_func())
