class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Shop:
    def __init__(self, filename):
        self.filename = filename

    def add_order(self, user, products):
        total = sum(p.price for p in products)
        names = ",".join([p.name for p in products])

        with open(self.filename, "a") as f:
            f.write(f"{user};{names};{total}\n")

    def show_orders(self):
        with open(self.filename, "r") as f:
            for line in f:
                user, products, total = line.strip().split(";")
                print(user, products, total)


p1 = Product("Laptop", 3000)
p2 = Product("Mouse", 100)

shop = Shop("orders.txt")

shop.add_order("Anna", [p1, p2])
shop.show_orders()
