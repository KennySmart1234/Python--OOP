import unittest

from stock import Stock

class MyTestCase(unittest.TestCase):
    def test_something(self):
        Stock("GTCO", "Guaranteed co", 100.0, 75.0)

    def test_get_symbol_returns_correct_symbol(self):
        stock_one = Stock("GTCO", "Guaranteed co", 100.0, 75.0)
        self.assertEqual("GTCO", stock_one.get_symbol() )


    def test_get_name_returns_correct_name(self):
        stock_one = Stock("GTCO", "Guaranteed co", 100.0, 75.0)
        self.assertEqual("Guaranteed co", stock_one.get_name())

    def test_symbol_is_not_case_sensitive(self):
        stock_one = Stock("gTcO", "Guaranteed co", 100.0, 75.0)
        self.assertEqual("GTCO", stock_one.get_symbol())

    def test_to_get_closing_price(self):
        stock = Stock("GTCO", "Guaranteed co", 100.0, 75.0)
        self.assertEqual(100.0, stock.get_closing_price())


    def test_to_get_current_price(self):
        stock = Stock("GTCO", "Guaranteed co", 100.0, 75.0)
        self.assertEqual(75.0, stock.get_current_price())




if __name__ == '__main__':
    unittest.main()
