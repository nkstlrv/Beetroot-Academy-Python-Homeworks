import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time --> {round((end-start), 3)}")
        return res
    return wrapper




