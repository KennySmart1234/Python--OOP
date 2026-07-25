
from src.product import Product
from src.cart import Cart
from src.checkout import Checkout
from src.invoice import Invoice


def main():
    print("=" * 40)
    print("      WELCOME TO CHECKOUT APP")
    print("=" * 40)

    cart = Cart()

    while True:
        product_name = input("\nEnter product name: ")

        while True:
            try:
                product_price = float(input("Enter product price: "))

                product = Product(product_name, product_price)
                cart.add_product(product)
                break

            except ValueError as e:
                print(f"Error: {e}")
                continue

        add_more = input("Add another product? (y/n): ").strip().lower()

        if add_more != "y":
            break



    while True:
        remove = input("Remove product? (y/n): ").strip().lower()
        if remove == "y":
            remove_product = input("\nEnter product name: ").strip().lower()
            for product in cart.products:
                if product.product_name == remove_product:
                    cart.remove_product(product)
                    print("\nProduct removed.")
                    break

            else:
                print("Invalid product name.")
        if remove == "n":
            break



    if cart.get_quantity() == 0:
        print("\nNo products in the cart.")
        return

    checkout = Checkout(cart)

    while True:
        try:
            amount_paid = float(input("\nEnter amount paid: "))
            checkout.calculate_balance(amount_paid)

            break

        except ValueError as e:
            print(e)
            print("Invalid amount.")

    invoice = Invoice(cart, checkout)

    print()
    print(invoice.generate_invoice(amount_paid))


if __name__ == "__main__":
    main()
