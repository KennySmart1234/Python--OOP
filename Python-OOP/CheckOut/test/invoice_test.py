import pytest

from src.cart import Cart
from src.checkout import Checkout
from src.invoice import Invoice



class TestInvoice:
    def test_that_invoice_can_be_created(self):
        cart = Cart()
        checkout = Checkout(cart)

        invoice = Invoice(cart, checkout)
        assert invoice is not None


    def test_invoice_stores_cart(self):
        cart = Cart()
        checkout = Checkout(cart)
        invoice = Invoice(cart, checkout)

        assert invoice.cart == cart


    def test_that_invoice_stores_checkout(self):
        cart = Cart()
        checkout = Checkout(cart)
        invoice = Invoice(cart, checkout)

        assert invoice.checkout == checkout


    def test_that_generate_invoice_receipt_returns_receipt(self):
        cart = Cart()
        checkout = Checkout(cart)
        invoice = Invoice(cart, checkout)

        receipt = invoice.generate_invoice(200.0)

        assert receipt is not None








