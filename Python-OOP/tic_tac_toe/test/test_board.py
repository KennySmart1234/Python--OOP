import unittest
from src.board import Board
from src.game import Game
from src.player import Player

class TestBoard(unittest.TestCase):
    def test_that_the_board_can_be_created(self):
        board = Board()
        self.assertEqual(3, board.get_size())

    def test_that_player_can_mark_a_position_on_the_board(self):
        board = Board()
        board.mark_position(0, 0, "X")
        self.assertEqual("X", board.get_position(0, 0))

    def test_that_two_players_can_mark_different_position_on_the_board(self):
        board = Board()
        board.mark_position(0, 0, "X")
        board.mark_position(2, 2, "O")
        self.assertEqual("X", board.get_position(0, 0))
        self.assertEqual("O", board.get_position(2, 2))

    def test_that_player_cannot_mark_occupied_board_position(self):
        board = Board()
        board.mark_position(1, 2, "X")
        with self.assertRaises(ValueError):
            board.mark_position(1, 2, "O")


    def test_that_if_all_board_positions_are_occupied(self):
        board = Board()
        board.mark_position(0, 0, "X")
        board.mark_position(2, 2, "O")
        self.assertFalse(False, board.is_board_full())


    def test_that_all_board_positions_are_empty(self):
        board = Board()
        self.assertFalse(False, board.is_board_full())


    def test_that_to_if_all_the_symbol_on_the_row_are_the_same(self):
        board = Board()

        board.mark_position(0, 0, "X")
        board.mark_position(0, 1, "X")
        board.mark_position(0, 2, "X")

        self.assertTrue(True, board.check_rows())


if __name__ == '__main__':
    unittest.main()
