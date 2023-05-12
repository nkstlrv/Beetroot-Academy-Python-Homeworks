# Task 3

# Using python as a calculator.

# Make a program with 2 numbers saved in separate variables a and b, then print the result
# for each of the following:

# Addition
# Subtraction
# Division
# Multiplication
# Exponent (Power)
# Modulus
# Floor division

# I wil use print("") to skip a line after each operation for convenience

import math

a = 3
b = 5.087

op_1 = "Addition"
op_2 = "Subtraction"
op_3 = "Division"
op_4 = "Multiplication"
op_5 = "Exponent (Power)"
op_6 = "Modulus"
op_7 = "Floor division"

print("1)", op_1, end= "--> \n")
print("a + b = ", a+b)

print("")

print("2)", op_2, end= "--> \n")
print("a - b = ", a - b, "\n", "b - a = ", b - a)

print("")

print("3)", op_3, end= "--> \n")
print("a / b = ", a / b, "\n", "b / a = ", b / a)

print("")

print("4)", op_4, end= "--> \n")
print("a x b = ", a * b)

print("")

print("5)", op_5, end= "--> \n")
print("a^b = ", a ** b, "\n", "b^a = ", b ** a)

print("")

print("6)", op_6, end= "--> \n")
print("a % b = ", a % b, "\n", "b % a = ", b % a)

print("")

print("7)", op_7, end= "--> \n")
print("a // b = ", a // b, "\n", "b // a = ", b // a)

