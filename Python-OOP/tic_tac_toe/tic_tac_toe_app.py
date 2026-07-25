from tic_tac_toe.player import Player
from tic_tac_toe.game import TicTacToeGame

def display_board(board):
    for row in range(board.get_size()):
        print(" | ".join(board.grid[row]))

        if row < board.get_size() - 1:
            print("---------")


def main():
    print("Welcome to Tic-Tac-Toe!")

    player_one_name = input("Enter Player 1 name: ")
    player_two_name = input("Enter Player 2 name: ")

    player_one = Player(player_one_name, "X")
    player_two = Player(player_two_name, "O")

    game = TicTacToeGame(player_one, player_two)

    while not game.is_game_over():

        display_board(game.get_board())

        current_player = game.get_current_player()

        print(
            f"\n{current_player.get_name()}'s turn "
            f"({current_player.get_symbol()})"
        )

        row = int(input("Enter row (0, 1, or 2): "))
        column = int(input("Enter column (0, 1, or 2): "))

        try:
            result = game.play(row, column)

            if result:
                display_board(game.get_board())
                print(result)

        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()