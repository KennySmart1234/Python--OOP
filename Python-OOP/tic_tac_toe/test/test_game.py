import unittest

from player import Player
from game import TicTacToeGame

class TestTicTacToeGame(unittest.TestCase):

    def setUp(self):
        self.player_one = Player("Kenny", "X")
        self.player_two = Player("Smart", "O")

        self.game = TicTacToeGame(
            self.player_one,
            self.player_two
        )

    def test_that_game_can_be_created(self):
        self.assertIsNotNone(self.game)

    def test_that_game_has_a_board(self):
        self.assertIsNotNone(self.game.get_board())

    def test_that_player_one_starts_the_game(self):
        self.assertEqual(
            self.player_one,
            self.game.get_current_player()
        )

    def test_that_player_can_play_on_the_board(self):
        self.game.play(0, 0)

        self.assertEqual(
            "X",
            self.game.get_board().get_position(0, 0)
        )

    def test_that_players_can_take_turns(self):
        self.game.play(0, 0)

        self.assertEqual(
            self.player_two,
            self.game.get_current_player()
        )

        self.game.play(1, 1)

        self.assertEqual(
            self.player_one,
            self.game.get_current_player()
        )

    def test_that_player_one_can_win(self):
        self.game.play(0, 0)  # X
        self.game.play(1, 0)  # O
        self.game.play(0, 1)  # X
        self.game.play(1, 1)  # O
        result = self.game.play(0, 2)  # X wins

        self.assertEqual(
            "Kenny wins",
            result
        )

    def test_that_winner_score_is_incremented(self):
        self.game.play(0, 0)
        self.game.play(1, 0)
        self.game.play(0, 1)
        self.game.play(1, 1)
        self.game.play(0, 2)

        self.assertEqual(
            1,
            self.player_one.get_score()
        )

    def test_that_game_is_over_when_player_wins(self):
        self.game.play(0, 0)
        self.game.play(1, 0)
        self.game.play(0, 1)
        self.game.play(1, 1)
        self.game.play(0, 2)

        self.assertTrue(
            self.game.is_game_over()
        )

    def test_that_player_cannot_play_after_game_is_over(self):
        self.game.play(0, 0)
        self.game.play(1, 0)
        self.game.play(0, 1)
        self.game.play(1, 1)
        self.game.play(0, 2)

        with self.assertRaises(ValueError):
            self.game.play(2, 2)


if __name__ == '__main__':
    unittest.main()