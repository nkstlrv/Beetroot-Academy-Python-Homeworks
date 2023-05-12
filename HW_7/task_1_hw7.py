# Task 1
#
# Make a program that has some sentence (a string)
# on input and returns a dict containing all unique words
# as keys and the number of occurrences as values.

result_dict = {}

usr_sentence = input("\n Enter any sentence, for example ('hello there'): ")
input_list = usr_sentence.split()
print("\n Input list is -->", input_list)

transfer_copy = input_list.copy()
index_list = transfer_copy

for i, item in enumerate(index_list):
    index_list[i] = (i + 1)
print("\n Index list is -->", index_list)

x = 0

while len(index_list) > x:
    result_dict.update({input_list[x]: index_list[x]})
    x += 1
print("\n Result dictionary is -->", result_dict)


