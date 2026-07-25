from src.cart import Cart


class Checkout:
    def __init__(self, cart: Cart):
        self.cart = cart

    def calculate_vat(self):
        subtotal = self.cart.calculate_subtotal()
        return subtotal * 0.075

    def calculate_total(self):
        return self.calculate_vat() + self.cart.calculate_subtotal()

    def amount_paid_validation(self, amount_paid):

        if amount_paid < self.calculate_total():
            raise ValueError("Insufficient payment")

        else:
            return amount_paid

    def calculate_balance(self, amount_paid):
        if not self.amount_paid_validation(amount_paid):
            raise ValueError("Insufficient payment")

        balance = amount_paid - self.calculate_total()
        return balance


