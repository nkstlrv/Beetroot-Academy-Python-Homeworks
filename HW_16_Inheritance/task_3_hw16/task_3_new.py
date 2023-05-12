class Product:

    def __init__(self, pr_type, name, price):
        self.pr_type = pr_type
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


p_1 = Product("test", "test", 0)


class ProductsQuantity:

    def __init__(self, product, amount, discount):
        self.product = product
        self.amount = amount
        self.discount = discount

    def __str__(self):
        return f"{self.product}"


pq_1 = ProductsQuantity(p_1, 0, 1.0)


class Market:
    markup = 1.30

    def __init__(self):
        self.stock: list[ProductsQuantity] = [pq_1]
        self.income = 0

    def get_all_products(self):
        for ind, item in enumerate(self.stock):
            print(f"{ind + 1} -- {item.product.pr_type}, {item.product.name}, Price - {item.product.price}, "
                  f"Amount - {item.amount}")

    def add_product(self, pr_type, name, price, amount, discount):
        for item in self.stock:
            if item.product.name == name:
                item.amount += amount
                break
            else:
                self.stock.append(ProductsQuantity(Product(pr_type, name, price), amount, discount))
                break

    def sell_product(self, name, amount):
        test_list = []
        for item in self.stock:
            if item.product.name == name:
                test_list.append(item)
                if item.amount < amount:
                    raise ValueError("There are no this quantity of items")
                else:
                    item.amount -= amount
                    price = item.product.price
                    discount = item.discount
                    self.income = price * self.markup * discount * amount
                    print(f"Product is sold. Your income is {self.income}")
                    break
        if len(test_list) == 0:
            raise ValueError("There are no this product in the store")

    def set_discount(self, product, discount):
        test_list = []
        for item in self.stock:
            if product == item.product.name:
                test_list.append(item)
                item.discount = discount
                print(f"Discount for {item.product.name} product is set -- {discount}")
                break
        if len(test_list) == 0:
            raise ValueError("There are no this product in the store")

    def get_income(self):
        print(f"Your total income is {self.income}")

    def get_product_info(self, product):
        test_list = []
        for item in self.stock:
            if product == item.product.name:
                test_list.append(item)
                print(f"Here is product info:\n"
                      f"Type -- {item.product.pr_type}\n"
                      f"Name -- {item.product.name}\n"
                      f"Price -- {item.product.price}\n"
                      f"Discount -- {item.discount}\n"
                      f"Amount -- {item.amount}")
                break
        if len(test_list) == 0:
            raise ValueError("There are no this product in the store")


m_1 = Market()
m_1.get_all_products()

m_1.add_product("plane", "cessna", 200, 15, 1.10)
m_1.get_all_products()

m_1.add_product("plane", "boeing", 1000, 5, 1.25)
m_1.get_all_products()
print("*" * 100)

m_1.sell_product("boeing", 2)
m_1.get_all_products()
print("*" * 100)

m_1.set_discount("cessna", 1.15)
print("*" * 100)

m_1.get_income()
print("*" * 100)

m_1.get_product_info("boeing")
