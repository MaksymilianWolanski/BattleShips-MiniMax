import random

from board import Board


def evaluate_move(board, x, y):
    """
    Prosta heurystyka Minimax.
    AI preferuje pola obok trafień.
    """

    score = 0

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 5 and 0 <= ny < 5:
            if board.grid[nx][ny] == "X":
                score += 10

    return score


def minimax_ai_move(player_board):
    best_score = -999
    best_move = None

    for i in range(5):
        for j in range(5):

            if player_board.grid[i][j] in ["O", "X"]:
                continue

            score = evaluate_move(player_board, i, j)

            if score > best_score:
                best_score = score
                best_move = (i, j)

    if best_move is None:
        while True:
            x = random.randint(0, 4)
            y = random.randint(0, 4)

            if player_board.grid[x][y] not in ["O", "X"]:
                return x, y

    return best_move


def setup_player_board():
    board = Board()

    print("Ustaw swoje 2 statki.")

    ships_placed = 0

    while ships_placed < 2:
        board.display()

        try:
            x = int(input("Wiersz: "))
            y = int(input("Kolumna: "))

            if board.place_ship(x, y):
                ships_placed += 1
            else:
                print("Tam już coś jest!")

        except:
            print("Nieprawidłowe dane.")

    return board


def setup_ai_board():
    board = Board(hide_ships=True)

    ships_placed = 0

    while ships_placed < 2:
        x = random.randint(0, 4)
        y = random.randint(0, 4)

        if board.place_ship(x, y):
            ships_placed += 1

    return board


def player_turn(ai_board):
    print("=== TWOJA TURA ===")

    while True:
        try:
            x = int(input("Wiersz: "))
            y = int(input("Kolumna: "))

            result = ai_board.shoot(x, y)

            if result == "hit":
                print("Trafiony!")
                break

            elif result == "miss":
                print("Pudło!")
                break

            else:
                print("Już strzelałeś w to miejsce.")

        except:
            print("Nieprawidłowe dane.")


def ai_turn(player_board):
    print("=== TURA AI ===")

    x, y = minimax_ai_move(player_board)

    print(f"AI strzela w: {x}, {y}")

    result = player_board.shoot(x, y)

    if result == "hit":
        print("AI trafiło!")

    else:
        print("AI spudłowało!")


def main():
    print("STATKI - MINIMAX AI")

    player_board = setup_player_board()
    ai_board = setup_ai_board()

    while True:

        print("\n=== TWOJA PLANSZA ===")
        player_board.display()

        print("=== PLANSZA PRZECIWNIKA ===")
        ai_board.display()

        player_turn(ai_board)

        if ai_board.remaining_ships() == 0:
            print("Wygrałeś!")
            break

        ai_turn(player_board)

        if player_board.remaining_ships() == 0:
            print("AI wygrało!")
            break


if __name__ == "__main__":
    main()