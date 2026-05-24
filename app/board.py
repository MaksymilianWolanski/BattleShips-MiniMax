BOARD_SIZE = 5


class Board:
    def __init__(self, hide_ships=False):
        self.hide_ships = hide_ships
        self.grid = [["~" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def display(self):
        print()

        print("  0 1 2 3 4")

        for i, row in enumerate(self.grid):
            row_display = []

            for cell in row:
                if self.hide_ships and cell == "S":
                    row_display.append("~")
                else:
                    row_display.append(cell)

            print(f"{i} " + " ".join(row_display))

        print()

    def place_ship(self, x, y):
        if self.grid[x][y] == "~":
            self.grid[x][y] = "S"
            return True

        return False

    def shoot(self, x, y):
        if self.grid[x][y] == "S":
            self.grid[x][y] = "X"
            return "hit"

        if self.grid[x][y] == "~":
            self.grid[x][y] = "O"
            return "miss"

        return "already"

    def remaining_ships(self):
        count = 0

        for row in self.grid:
            count += row.count("S")

        return count