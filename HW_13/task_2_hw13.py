
def lists_multiplier(list_1: list):
    def multiply(list_2):
        result = [item_1 * item_2 for item_1, item_2 in zip(list_1, list_2)]
        return result
    return multiply

outer_func = lists_multiplier([1, 2, 3, 4])

# Multiplies to lists so we've got access to the inner function
inner_func = outer_func([4, 3, 2, 1])
print(inner_func)



def outer_func(name: str):
    def inner_func():
        text = f"\n Hello there, {name}!"
        return text
    return inner_func()

# Uses inner text, so we've got access to the nested functions
a = outer_func("Beetroot")
print(a)

