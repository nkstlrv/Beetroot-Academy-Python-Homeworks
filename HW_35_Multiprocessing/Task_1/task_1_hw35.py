import time
import concurrent.futures

NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time --> {round((end-start), 3)} sec")
        return res
    return wrapper


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


@timer
def simple_execution():

    bools = []

    for n in NUMBERS:
        bools.append(is_prime(n))
    return bools


@timer
def threading_execution():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(is_prime, NUMBERS)


@timer
def processing_execution():
    with concurrent.futures.ProcessPoolExecutor() as p_executor:
        p_executor.map(is_prime, NUMBERS)


if __name__ == "__main__":

    print(simple_execution())

    threading_execution()

    processing_execution()


