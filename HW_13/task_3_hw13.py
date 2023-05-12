
# Our lists
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

# Function 1
def square_nums(nums):
    return [num ** 2 for num in nums]

# Function 2
def remove_negatives(nums):
    return [num for num in nums if num > 0]


# Main function
def choose_func(nums: list, func1, func2):
    check_list = [item for item in nums if item <0]
    if len(check_list) == 0:
        return func1
    else:
        return func2

# List with positive nums only
p = choose_func(nums1, square_nums(nums1), remove_negatives(nums1))
print(p)

# List with negative nums
n = choose_func(nums2, square_nums(nums2), remove_negatives(nums2))
print(n)