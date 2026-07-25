
class Cart:
    def __init__(self):
        self.products = []
        self.quantity = 0


    def get_quantity(self):
        return self.quantity


    def add_product(self, product):
        self.products.append(product)
        self.quantity += 1

    def remove_product(self, product_one):
        self.products.remove(product_one)
        self.quantity -= 1

    def get_product(self, index):
        return self.products[index]

    def calculate_subtotal(self):
        subtotal = 0.0
        for product in self.products:
            subtotal += product.product_price

        return subtotal


    def clear_cart(self):
        self.products.clear()
        self.quantity = 0


