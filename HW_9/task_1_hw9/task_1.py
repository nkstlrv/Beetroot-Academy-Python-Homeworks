# Task 1
#
# Imports practice

# Make a directory with 2 modules; make a function in one of them;
# then import this function in the other module and use that in your script of choice.

from list_math import lst_add, lst_sub, lst_div, lst_mult

print("\n Hello there!"
      "\n This script simply makes basic mathematics operations with given list of integers.")

# Tried to do this script with while/for-in loops with data types checks, etc...
# but unfortunately I had problems with exiting the nested loops
usr_numbers = input("\n ENTER integers, separated by coma: ")

usr_input_list = usr_numbers.split(",")
arguments_list = []

for i, item in enumerate(usr_input_list):
    if item != " " and item != ",":
        arguments_list.append(int(item))
print("\n Your arguments list is -->", arguments_list)

usr_operation = str(input("\n Now I need to know which operation do you want to use"
                          "\n Just type ADD, SUBTRACT, MULTIPLY or DIVIDE"
                          "\n\n What is your answer?: "))

if usr_operation.upper() == "ADD":
    print("\n Your answer is -->", lst_add(arguments_list))
elif usr_operation.upper() == "SUBTRACT":
    print("\n Your answer is -->", lst_sub(arguments_list))
elif usr_operation.upper() == "MULTIPLY":
    print("\n Your answer is -->", lst_mult(arguments_list))
elif usr_operation.upper() == "DIVIDE":
    print("\n Your answer is -->", lst_div(arguments_list))

else:
      print("\n There is no such operation :("
            "\n Try again")
