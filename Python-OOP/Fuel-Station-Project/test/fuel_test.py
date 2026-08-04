
import pytest
from src.fuel import Fuel


class TestFuel:
    def test_that_fuel_is_created_quantity_is_50(self):
        fuel = Fuel("Petrol", 500.0, 50)
        assert fuel.get_quantity == 50.0
        assert fuel.get_price == 500.0


    # def test_that_fuel_is_created_quantity_cannot_below_50(self):
    #     #pytest.raises(ValueError, lambda: Fuel("Petrol", 500.0, 45.0))
    #     with pytest.raises(ValueError):
    #         Fuel("Petrol", 500.0, 45.0)


    # def test_that_fuel_price_cannot_below_100(self):
    #     with pytest.raises(ValueError):
    #         Fuel("Petrol", 100.0, 45.0)
    #
    #
    # def test_that_fuel_price_isRetrived(self):
    #     fuel = Fuel("Petrol", 500.0, 45.0)
    #     assert fuel.get_fuel_type("Petrol")

