from src.fuel import Fuel


class Dispenser:
    def __init__(self):
        self._number_of_fuel = 0
        self._fuels = {}

    def get_number_of_fuel(self):
        return self._number_of_fuel


    def create_fuel(self, type, price, quantity):
        new_fuel = Fuel(type, price, quantity)
        self._fuels[type] = new_fuel

        self._number_of_fuel += 1
        return new_fuel


    def get_available_type(self):
        return [fuel for fuel in self._fuels]



    def update_fuel_price(self, type, price):
        fuel = self._fuels[type]
        fuel._price = price
        return fuel

