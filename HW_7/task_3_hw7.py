# Task 3

# List comprehension exercise
#
# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.


print("\n Task done WITH usage of list comprehension:")

lst_ij_comp = [(j, j**2) for i, j in enumerate(range(1, 11))]
print(lst_ij_comp)

print("\n Task done without list comprehension:")

lst_ij = []
for i, j in enumerate(range(1, 11)):
    lst_ij.append((j, j**2))
print(lst_ij)
