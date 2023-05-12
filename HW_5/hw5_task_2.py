# Task 2
#
# The birthday greeting program.
#
# Write a program that takes your name as input, and then your
# age as input and greets you with the following:
#
# “Hello <name>, on your next birthday you’ll be <age+1> years”

print("\nHello! This is a Birthday greeting program!\n")

while True:

    ur_name = input("What is your name?: ")

    if ur_name.isdigit():
        print("\nEnter letters only? please\n")
        continue
    else:
        ur_name = ur_name.title()
        print(f"\nNice to meet you {ur_name}!\n")

        ur_age = input("How old are you?: ")

        if ur_age.isalpha():
            print("\nEnter numbers only, please\n")
            continue
        else:
            nxt_year = int(ur_age) + 1
            print("\nWow, you look so young! :)\n",
                  f"\nBy the way...the next year you will be {nxt_year} years old")
            break
