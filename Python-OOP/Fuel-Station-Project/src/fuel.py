
class Fuel:
    def __init__(self, fuel_type, price, quantity = 50.0):
        if quantity < 50:
            raise ValueError("Quantity should not be below 50")
        elif quantity < 100:
            raise ValueError("Fuel Prices should not be less than 100")

        self._fuel_type = fuel_type
        self._price = price
        self._quantity = quantity

    def get_fuel_type(self):
        return self._fuel_type

    def set_price(self, price):
        if price < 100:
            raise ValueError("Price must be less than 100")
        self._price = price

    def get_price(self):
        return self._price



    def get_quantity(self):
        return self._quantity
