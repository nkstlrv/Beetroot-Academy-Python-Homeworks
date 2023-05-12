# from functools import wraps

# Couldn't do this task with wraps module, "TypeError: 'int' object is not iterable" is being called

def arg_rules(type_, max_length, contains):
    # @wraps(type_, max_length, contains)
    def wrapper(func):
        new_lst = [item for item in contains if isinstance(item, type_) and len(item) <= max_length]
        if len(new_lst) ==0:
            return False
        else:
            return func(new_lst[0])
    return wrapper


@ arg_rules(type_ = str, max_length = 15, contains = [1, 2, [22, "aars"]])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
print(create_slogan)


@ arg_rules(type_ = str, max_length = 15, contains = [1, 2, [22, "aars"], "Python"])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
print(create_slogan)