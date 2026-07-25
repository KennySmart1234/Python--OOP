
import pytest

from src import fuel
from src.dispenser import Dispenser

class TestDispenser:

    @pytest.fixture
    def dispenser(self):
        return Dispenser()

    def test_that_dispenser_has_no_fuel(self):
        assert dispenser.get_number_of_fuel() == 0;


    def test_that_dispenser_has_fuel(self, dispenser):
        assert dispenser.get_number_of_fuel() == 0;
        fuel = dispenser.create_fuel("Petrol", 500.0)
        assert dispenser.get_number_of_fuel() == 1
        assert fuel.get_fuel_type() == "Petrol"

    def test_that_Avialable_fuel_are_retrieved(self, dispenser):
        assert dispenser.get_number_of_fuel() == 0
        fuel_one = dispenser.create_fuel("Petrol", 500.0)
        fuel_two = dispenser.create_fuel("Gas", 500.0)

        assert dispenser.get_number_of_fuel() == 2
        assert dispenser.get_available_type() == ["Petrol", "Gas"]


    def test_that_dispenser_can_update_fuel_price(self, dispenser):

        fuel_one = dispenser.create_fuel("Petrol", 500.0)
        fuel_two = dispenser.create_fuel("Gas", 500.0)

        assert dispenser.get_number_of_fuel() == 2
        assert fuel_one.get_price() == 500.0
        assert fuel_two.get_price() == 300.0





