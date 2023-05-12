# Task 1
#
# The Guessing Game.
#
# Write a program that generates a random number between 1 and 10 and lets the user guess
# what number was generated. The result should be sent back to the user via a print statement.

###############################################################################################

# Help!
# Need the program to check the input string,
# if there are anything except numbers, program will ask to repeat the entering
# also if there will be float numbers like (2.0) or (2.3), program
# will convert it into integer

import random

print("\nguess the number game \n\n".upper(),
      ("Instructions:\n"
       "        Type a number from 1 to 10, \n"
       "        using INTEGERS only,\n"
       "        and then, press Enter. \n\n"
       "       "))

while True:

    usr_answer = input("Enter your answer, please: ")

    if usr_answer.isalpha():
        print("\nINTEGER numbers only\n")
        continue

    else:
        usr_answer = int(usr_answer)
        correct_answer = random.randint(1, 10)

        if usr_answer == correct_answer:
            print("\n! Victory !\n".upper())
            break
        else:
            print("\nYou've lost :(\n",
                  f"Correct answer was --> {correct_answer}")
            break
