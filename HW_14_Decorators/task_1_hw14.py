# Task 1
# Write a decorator that prints a function with arguments passed to it.
# note! It should print the function, not the result of its execution!

from functools import wraps

def decorator_task_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function name is --> {func.__name__}")
        print(f"Passed-in arguments are --> {args}, {kwargs}")
    return wrapper

# Function before decoration
def main_func(name, something, a, b):
    print(name, something)
    return a ** b

# Execution of this function
print(main_func('test', 'hello world', b = 4, a = 5))

print("\n")

# Decoration 
@ decorator_task_1
def main_func(name, something, a, b):
    print(name, something)
    return a ** b

# Execution of the decorated function 
main_func('test', 'hello world', a = 4, b = 5)


