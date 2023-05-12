# Task 2
#
# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).


def task_2_func():
    while True:
        try:
            a = float(input("\n Enter FIRST number: "))
            b = float(input("\n Now, enter the SECOND one: "))
        except ValueError:
            print("\n ERROR:"
                  "\n Use numbers only")
            continue
        try:
            a / b
        except ZeroDivisionError:
            print("\n ERROR:"
                  "You can't divide by zero")
            continue
        return print(a**2/b)


task_2_func()
