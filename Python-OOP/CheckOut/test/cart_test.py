import pytest
from src.cart import Cart
from src.product import Product


class TestCart:
    def test_that_product_list_is_empty(self):
        cart = Cart()
        assert cart.products == []


    def test_that_one_product_is_added_to_the_cart_and_count_one(self):
        cart = Cart()
        product = Product("Rice", 100)
        cart.add_product(product)
        assert len(cart.products) == 1
        assert cart.get_quantity() == 1




    def test_that_five_products_are_added_to_the_cart_and_count_five(self):

        cart = Cart()
        product_one = Product("Rice", 1000.0)
        product_two = Product("Bread", 80.0)
        product_three = Product("beans", 90.0)
        product_four = Product("Butter", 90.0)
        product_five = Product("water", 20.0)

        cart.add_product(product_one)
        cart.add_product(product_two)
        cart.add_product(product_three)
        cart.add_product(product_four)
        cart.add_product(product_five)
        assert len(cart.products) == 5
        assert cart.get_quantity() == 5

    def test_that_two_product_added_two_product_removed_count_is_zero(self):
        cart = Cart()
        product_one = Product("Rice", 100)
        product_two = Product("Bread", 80)

        cart.add_product(product_one)
        cart.add_product(product_two)
        assert len(cart.products) == 2

        cart.remove_product(product_one)
        cart.remove_product(product_two)

        assert len(cart.products) == 0
        assert cart.get_quantity() == 0

    def test_that_five_product_added_two_product_removed_count_is_three(self):
        cart = Cart()

        product_one = Product("Rice", 100.0)
        product_two = Product("Bread", 800.0)
        product_three = Product("beans", 90.0)
        product_four = Product("water", 20.0)
        product_five = Product("fufu", 2000.0)

        cart.add_product(product_one)
        cart.add_product(product_two)
        cart.add_product(product_three)
        cart.add_product(product_four)
        cart.add_product(product_five)
        assert len(cart.products) == 5
        assert cart.get_quantity() == 5

        cart.remove_product(product_one)
        cart.remove_product(product_two)

        assert len(cart.products) == 3
        assert cart.get_quantity() == 3


    def test_to_get_list_of_all_products(self):
        cart = Cart()
        product_one = Product("Rice", 100)
        product_two = Product("Bread", 80)
        product_three = Product("beans", 90)
        product_four = Product("water", 20.0)

        cart.add_product(product_one)
        cart.add_product(product_two)
        cart.add_product(product_three)
        cart.add_product(product_four)

        assert len(cart.products) == 4

        assert cart.get_product(0) == product_one
        assert cart.get_product(1) == product_two
        assert cart.get_product(2) == product_three
        assert cart.get_product(3) == product_four


    def test_to_add_three_products_removed_one_product_count_is_two(self):

        cart = Cart()
        product_one = Product("Rice", 100)
        product_two = Product("Bread", 80)
        product_three = Product("beans", 90)

        cart.add_product(product_one)
        cart.add_product(product_two)
        cart.add_product(product_three)

        assert len(cart.products) == 3

        cart.remove_product(product_one)
        assert len(cart.products) == 2

        assert cart.get_product(0) == product_two
        assert cart.get_product(1) == product_three

        assert cart.get_quantity() == 2




    def test_same_product_can_be_added_twice(self):
        cart = Cart()
        product_one = Product("Rice", 100)
        product_two = Product("Rice", 80)

        cart.add_product(product_one)
        cart.add_product(product_two)

        assert cart.get_product(0) == product_one
        assert cart.get_product(1) == product_two


    def test_that_cart_subtotal_calculation_is_zero(self):
            cart = Cart()
            assert cart.calculate_subtotal() == 0


    def test_to_calculate_subtotal_returns_correct_result(self):
            cart = Cart()
            product_one = Product("Rice", 100.0)
            product_two = Product("Bread", 50.0)
            product_three = Product("beans", 120.0)

            cart.add_product(product_one)
            cart.add_product(product_two)
            cart.add_product(product_three)

            assert cart.calculate_subtotal() == 270.0




    def test_to_clear_all_product_in_the_cart(self):
            cart = Cart()
            product_one = Product("Rice", 100.0)
            product_two = Product("Bread", 80.0)
            product_three = Product("beans", 90.0)
            cart.add_product(product_one)
            cart.add_product(product_two)
            cart.add_product(product_three)
            assert len(cart.products) == 3
            assert cart.get_quantity() == 3
            cart.clear_cart()
            assert len(cart.products) == 0
            assert cart.get_quantity() == 0

