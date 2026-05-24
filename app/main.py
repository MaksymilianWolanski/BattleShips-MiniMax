import random

from app.board import Board
from app.minimax import minimax_ai_move


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

        except ValueError:
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

            if result == "miss":
                print("Pudło!")
                break

            print("Już strzelałeś w to miejsce.")

        except ValueError:
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