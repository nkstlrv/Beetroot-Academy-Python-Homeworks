# Task 1

# The greatest number

# Write a Python program to get the largest number from a list of random 
# numbers with the length of 10

# Constraints: use only while loop and random module to generate numbers
#########################################################################


import random


lst = []

while True:

    lst.append(random.randint(-6, 4))
    
    if len(lst) == 10:
        
        print("Our random list is --", lst)
        print("List length is --", len(lst))

        gr_num = max(lst)
        sm_num = min(lst)

        print("The largest number from the list is --", gr_num) 
        print("The smallest number from the list is --", sm_num)


        break



      
   
   


    


   
       







