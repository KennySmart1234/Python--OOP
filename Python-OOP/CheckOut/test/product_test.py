import pytest
from src.product import Product


class TestProduct:

    def test_that_product_name_and_price_can_be_returned(self):
        product = Product("Rice", 100.0)
        assert product.product_name == "rice"
        assert product.product_price == 100.0


    def test_to_add_more_than_one_product_and_price(self):
        product_one = Product("Pizza", 1000.0)
        product_two = Product("Plantain", 1500.0)

        assert product_one.product_name == "pizza"
        assert product_one.product_price == 1000.0

        assert product_two.product_name == "plantain"
        assert product_two.product_price == 1500.0


    def test_that_product_name_is_not_case_sensitive(self):
        product_one = Product("EgUsi", 1000.0)
        product_two = Product("plaNtaIn", 1500.0)

        assert product_one.product_name == "egusi"
        assert product_two.product_name == "plantain"



    def test_that_product_price_can_be_zero(self):
        product_one = Product("Suya", 0.0)
        product_two = Product("Fish", 0.0)

        assert product_one.product_price == 0.0
        assert product_two.product_price == 0.0


    def test_that_product_price_can_not_be_less_than_zero(self):
        with pytest.raises(ValueError):
            Product("Beans", -3.0)


    def test_that_product_name_can_not_be_empty_string(self):
        with pytest.raises(ValueError):
            Product("   ", 7.0)


    def test_that_product_price_should_be_a_number(self):
        Product("Rice", 100.0)

        with pytest.raises(TypeError):
            Product("Pizza", "One Hundred Naira")






