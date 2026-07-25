class Player:

    VALID_SYMBOL = ("X", "O")

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = None
        self.set_symbol(symbol)
        self.score = 0

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_score(self):
        return self.score

    def set_name(self, name):
        if not name:
            raise ValueError("Player must have a name")
        else:
            self.name = name

    def set_symbol(self, symbol):
        symbol = symbol.upper()
        if symbol not in Player.VALID_SYMBOL:
            raise ValueError(f"Symbol must be one of {Player.VALID_SYMBOL}")
        else:
            self.symbol = symbol.upper()

    def increment_score(self):
        self.score += 1

    def __str__(self):
        return f"Player {self.name}, {self.symbol}, {self.score}"

    def __repr__(self):
        return f"Player(name= {self.name}, sysmbol={self.symbol}, {self.score})"