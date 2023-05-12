# Task 2

# Exclusive common numbers.

# Generate 2 lists with the length of 10 with random integers from 1 to 10, 
# and make a third list containing the common integers between the 2 
# initial lists without any duplicates.

# Constraints: use only while loop and random module to generate numbers
#########################################################################

import random


lst_1 = []
lst_2 = []

while True:

    lst_1.append(random.randint(1, 10))
    lst_2.append(random.randint(1, 10))

    if len(lst_1) and len(lst_2) == 10:

        print(lst_1)
        print(lst_2)

        st_1 = set(lst_1)
        st_2 = set(lst_2)

        print("\n", st_1)
        print(st_2)
        
        lst_3 = list(st_1.intersection(st_2))

        print("\n Common integers in both lists --", lst_3)

        break