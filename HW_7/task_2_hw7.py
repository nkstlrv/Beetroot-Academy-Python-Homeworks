# Task 2

# Input data:
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }

# Compute the total price of the stock
# where the total price is the sum of the price of an item
# multiplied by the quantity of this exact item.


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "pear": 3,
    "orange": 1.5,

}

total_stock_price = 0

items_list = [s for s in stock.keys()]
print("\n List of our items in the stock -->", items_list)

for item in items_list:
    total_stock_price += stock[item] * prices[item]

print("\n Answer is-->", total_stock_price)

# --------------------------------------------------------------------------
# Old solution:
#
# stock_list = []
# for s_val in stock.values():
#     stock_list.append(float(s_val))
# print("\n Our item's quantities list is -->", stock_list)
#
# prices_list = []
# for p_val in prices.values():
#     prices_list.append(float(p_val))
# print("\n Our item's prices list is -->", prices_list)
#
# set_prices_list = []
# for i in range(len(stock_list)):
#     set_prices_list.append(stock_list[i] * prices_list[i])
# print("\n Price of each set of items  -->", set_prices_list)
#
#
# total_price = sum(set_prices_list)
#
# print("\n Our stock total price is -->", total_price)
#
#
