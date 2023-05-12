# Task 4
#
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

import calendar

day_names = list(calendar.day_name)
print("\n List of the week days -->", day_names)

week_list = [d for d in day_names]

week_dict_one = {}

for ind, item in enumerate(week_list):
    week_dict_one.update({ind: item})
print("\n The first variant of dict -->", week_dict_one)

week_dict_two = {}

for ind, item in enumerate(week_list):
    week_dict_two.update({item: ind})
print("\n The second variant of dict -->", week_dict_two)

# ----------------------------------------------------------------------------
# Old solution:
# dict_1 = {}
# dict_2 = {}
#
# i_1 = 0
# i_2 = 0
#
# while len(week_list_1) > i_1:
#     dict_1.update({week_list_1[i_1][0]: week_list_1[i_1][1]})
#     i_1 += 1
# print("\n Our first dict -->", dict_1)
#
#
# while len(week_list_1) > i_2:
#     dict_2.update({week_list_1[i_2][1]: week_list_1[i_2][0]})
#     i_2 += 1
# print("\n Our second dict -->", dict_2)
