class Stock:
    def __init__(self, symbol:str, name:str, previous_closing_price:float, current_price:float):
        self.__symbol = None
        self.set_symbol(symbol)
        self.__name = name
        self.__previous_closing_price = previous_closing_price
        self.__current_price = current_price
        
    # this part is called decorator in python
    # and is doing setter and getter
    # __ (double underscore means private)

    @property
    def symbol(self):
        return self.__symbol
    @symbol.setter
    def symbol(self, symbol:str):
        self.__symbol = symbol.upper()

    @property
    def name(self):
        return self.__name

    # def get_symbol(self):
    #     return self.__symbol
    #
    # def set_symbol(self, symbol:str):
    #     self.__symbol = symbol.upper()
    #
    # def get_name(self):
    #     return self.__name

    def get_closing_price(self):
        return self.__previous_closing_price

    def set_closing_price(self, previous_closing_price:float):
        self.__previous_closing_price = previous_closing_price

    def get_current_price(self):
        return self.__current_price

    def set_current_price(self, current_price:float):
        self.__current_price = current_price








