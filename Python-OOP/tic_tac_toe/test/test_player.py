import unittest
from tic_tac_toe.player import Player


class TestPlayer(unittest.TestCase):
    def test_that_player_can_be_created(self):
        player = Player("Kenny", "X")

        self.assertEqual("Kenny", player.get_name())
        self.assertEqual("X", player.get_symbol())



    def test_that_two_players_can_be_created(self):
        player_one = Player("Kenny", "X")
        player_two = Player("Smart", "O")

        self.assertEqual("Kenny", player_one.get_name())
        self.assertEqual("X", player_one.get_symbol())
        self.assertEqual("Smart", player_two.get_name())
        self.assertEqual("O", player_two.get_symbol())

    def test_that_payer_pick_correct_system(self):
        player_one = Player("Kenny", "O")
        player_two = Player("Smart", "X")

        self.assertNotEqual("Y", player_one.get_symbol())
        self.assertNotEqual("N", player_two.get_symbol())


    def test_that_invalid_symbol_raises_value_error(self):
        with self.assertRaises(ValueError):
            Player("Kenny", "T")

if __name__ == '__main__':
    unittest.main()
