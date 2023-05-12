# Task 3

# Extracting numbers.

# Make a list that contains all integers from 1 to 100, 
# then find all integers from the list that are divisible by 7 
# but not a multiple of 5, and store them in a separate list. 
# Finally, print the list.

# Constraint: use only while loop for iteration
#################################################################


lst = list(range(1, 101))
print("Our original list is --", lst, "\n")
new_lst = []

i = 0

while True:
   
    if lst[i] % 7 ==0 and lst[i] % 5 != 0:
        new_lst.append(lst[i])

    elif lst[i] == 100:
        print("Our new list is --", new_lst)
        break
        
    i += 1
    

   

    

    