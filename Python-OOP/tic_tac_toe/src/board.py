class Board:

    def __init__(self):
        self.size = 3
        self.grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def get_size(self):
        return self.size

    def mark_position(self, row, column, symbol):
        if self.grid[row][column] != " ":
            raise ValueError("Position already occupied")

        self.grid[row][column] = symbol

    def get_position(self, row, column):
        return self.grid[row][column]

    def is_board_full(self):
        for row in self.grid:
            for position in row:
                if position == " ":
                    return False

        return True

    def check_row(self, row):
        position_one = self.grid[row][0]
        position_two = self.grid[row][1]
        position_three = self.grid[row][2]

        if (
            position_one != " "
            and position_one == position_two == position_three
        ):
            return True

        return False

    def check_rows(self):
        for row in range(self.size):
            if self.check_row(row):
                return True

        return False








