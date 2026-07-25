import pytest

from src.cart import Cart
from src.checkout import Checkout
from src.product import Product


class TestCheckout:
    def test_that_checkout_can_be_created(self):
        cart = Cart()
        checkout = Checkout(cart)

        assert checkout is not None


    def test_that_calculate_vat_returns_correct_value(self):
        cart = Cart()
        cart.add_product(Product("Rice", 100.0))
        cart.add_product(Product("Banana", 200.0))
        cart.add_product(Product("Orange", 300.0))

        checkout = Checkout(cart)

        assert checkout.calculate_vat() == 45.0


    def test_to_calculate_total_price_minus_vat(self):
        cart = Cart()
        cart.add_product(Product("Rice", 1000.0))
        cart.add_product(Product("Banana", 2000.0))
        cart.add_product(Product("Orange", 3000.0))

        checkout = Checkout(cart)
        assert checkout.calculate_total() == 6450.0


    def test_to_validate_payment_from_customer(self):
        cart = Cart()
        cart.add_product(Product("Rice", 1500.0))
        cart.add_product(Product("Banana", 1200.0))
        cart.add_product(Product("Orange", 5000.0))
        checkout = Checkout(cart)

        assert checkout.amount_paid_validation(8277.5) == 8277.5


    def test_that_insufficient_funds_raises_error(self):
        cart = Cart()
        cart.add_product(Product("Rice", 8800.0))
        cart.add_product(Product("Banana", 6200.0))
        cart.add_product(Product("Orange", 7000.0))

        checkout = Checkout(cart)

        with pytest.raises(ValueError):
            checkout.amount_paid_validation(-419.0)


    def test_process_payment_returns_correct_value(self):
        cart = Cart()
        cart.add_product(Product("Rice", 1000.0))
        cart.add_product(Product("Banana", 2000.0))
        cart.add_product(Product("Orange", 3000.0))
        checkout = Checkout(cart)

        assert checkout.calculate_balance(7000.0) == 550.0


    def test_that_balance_can_be_zero(self):

        cart = Cart()
        cart.add_product(Product("Rice", 100.0))
        cart.add_product(Product("Banana", 200.0))
        cart.add_product(Product("Orange", 300.0))
        checkout = Checkout(cart)

        assert checkout.calculate_balance(645.0) == 0.0
