# Prices are in thousands USD --> 100 = $100,000
class Product:

    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = self.price_validator(price)
        self.price = price

    def price_validator(self, price):
        if price < 0:
            raise ValueError("Price can not be negative")


class ProductStore(Product):
    discount = 5
    income = 0
    market = [
        {
            "Product": "Test",
            "Price": 0,
            "Amount": 0
        }
    ]

    def __init__(self, type, name, price, amount):
        self.amount = self.amount_validator(amount)
        self.amount = amount
        super().__init__(type, name, price)

        ProductStore.market.append(
            {
                "Product": self.name,
                "Price": self.price,
                "Amount": self.amount
            }
        )

    def amount_validator(self, amount):
        if amount < 0:
            raise ValueError("Amount can not be negative")

    def add_product(self, add_product, add_amount, add_price):
        ProductStore.market.append(
            {
                "Product": add_product,
                "Price": add_price,
                "Amount": add_amount
            }
        )
        return "Product added"

    def set_discount(self, discount):
        ProductStore.discount = discount

    def sell_product(self, sell_product, sell_amount):
        sell_list = []
        for item in ProductStore.market:
            if item["Product"] == sell_product:
                if sell_amount <= item["Amount"]:
                    sell_list.append(item)
                    item["Amount"] -= sell_amount
                    ProductStore.income = item["Price"] * sell_amount - (
                                item["Price"] * sell_amount * ProductStore.discount / 100)
                    break
                else:
                    raise ValueError("There are no so many products in the market")
        if len(sell_list) == 0:
            raise ValueError("No such product in the store")

    def get_income(self):
        return f" Your store total income is --> {self.income}"

    def get_all_products(self):
        return f"Here are all market products --> {ProductStore.market}"

    def get_product_info(self, product_name):
        find_lst = []
        for item in self.market:
            if item["Product"] == product_name:
                find_lst.append(item)
                break
        if len(find_lst) == 0:
            return "There no this product in the stock :("
        else:
            name = find_lst[0]["Product"]
            amount = find_lst[0]["Amount"]
            info = f" Here is product's info:", f" Name --> {name}", f" Amount of items --> {amount}"
            return info


a = ProductStore("planes", "Cessna", 100, 10)
a.add_product("Boeing", 2, 2000)
a.set_discount(25)

a.sell_product("Cessna", 2)
print(a.market)
print(a.income)

print(a.get_all_products())

print(a.get_product_info("Boeing"))
