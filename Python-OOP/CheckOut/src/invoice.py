
class Invoice:
    def __init__(self, cart, checkout):
        self.cart = cart
        self.checkout = checkout


    def get_cart(self):
        return self.cart

    def get_checkout(self):
        return self.checkout


    def generate_invoice(self, amount_paid):
        receipt = "========== Payment Receipt ==========\n"
        receipt += "Items\n"
        for product in self.cart.products:
            receipt += f"- {product.product_name} # {product.product_price:.2f}\n"

        receipt +="\n"
        receipt += f"Subtotal      :  #{self.cart.calculate_subtotal():.2f}\n"
        receipt += f"Total         :  #{self.checkout.calculate_total():.2f}\n"
        receipt += f"VAT           :  #{self.checkout.calculate_vat():.2f}\n"
        receipt += f"Amount paid   :  #{amount_paid:.2f}\n"
        receipt += f"Balance       :  #{self.checkout.calculate_balance(amount_paid):.2f}\n"

        receipt += "==========THANKS FOR YOUR PATRONAGE ==========\n"

        return receipt






