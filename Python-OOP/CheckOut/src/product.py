from itertools import product


class Product:
    def __init__(self, product_name, product_price):
        self.__product_name = None
        self.__product_price = None

        self.product_name = product_name
        self.product_price = product_price



    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):
        if product_name.strip() == "":
            raise ValueError("Product name cannot be empty")
        self.__product_name = product_name.strip().lower()


    @property
    def product_price(self):
        return self.__product_price

    @product_price.setter
    def product_price(self, product_price):
        if not isinstance(product_price, (float, int)):
            raise TypeError("Product price must be a number")

        if product_price < 0:
            raise ValueError("Product price cannot be negative")

        self.__product_price = float(product_price)


