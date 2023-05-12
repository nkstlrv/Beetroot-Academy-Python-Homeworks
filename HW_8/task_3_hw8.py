# Task 3
#
# A simple calculator.
#
# Create a function called make_operation,
# which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
# and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter.
#
# For example:
#
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42

# I tried to use same loop for all operations but unfortunately strange things happens with Division and Subtraction

# Multiplier
def multiplier(lst: list):
    res = 1
    for item in lst:
        res *= item
    return res

# Divider
def divider(lst: list):
    a = lst[0]
    for ind, item in enumerate(lst):
        if ind+1 ==len(lst):
            break
        if 0 in lst[1:]:
            print("You can't divide by zero")
            quit()
        a = a/lst[ind + 1]
    return a

# Power one by one
def power(lst: list):
     a = lst[0]
     for ind, item in enumerate(lst):
        if ind+1 ==len(lst):
            break
        if 0 in lst[1:]:
            print("You can't divide by zero")
            quit()
        a = a**lst[ind + 1]
     return a
   
# Main function
def list_calc(operator:str(), lst:list) -> int():
    if operator == "+":
        return print(adder(lst))
    elif operator == "-":
        return print(subtracter(lst))
    elif operator == "*":
        return print(multiplier(lst))
    elif operator == "/":
        return print(divider(lst))
    elif operator == "^":
        return print(power(lst))
    else:
        print("Unexpected math operator")


list_calc("^", [2, 2, 3])





