from board import Board
from player import Player


class TicTacToeGame:

    def __init__(self, player_one, player_two):
        self.board = Board()
        self.player_one = player_one
        self.player_two = player_two
        self.current_player = player_one
        self.game_over = False

    def get_board(self):
        return self.board

    def get_current_player(self):
        return self.current_player

    def switch_player(self):
        if self.current_player == self.player_one:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one

    def play(self, row, column):
        if self.game_over:
            raise ValueError("Game is already over")

        symbol = self.current_player.get_symbol()

        self.board.mark_position(row, column, symbol)

        if self.board.check_rows():
            self.current_player.increment_score()
            self.game_over = True
            return f"{self.current_player.get_name()} wins"

        if self.board.is_board_full():
            self.game_over = True
            return "Draw"

        self.switch_player()

    def is_game_over(self):
        return self.game_over