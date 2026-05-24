from app.board import Board


def test_place_ship():
    board = Board()

    result = board.place_ship(1, 1)

    assert result is True
    assert board.grid[1][1] == "S"


def test_place_ship_taken():
    board = Board()

    board.place_ship(1, 1)

    result = board.place_ship(1, 1)

    assert result is False


def test_shoot_hit():
    board = Board()

    board.place_ship(2, 2)

    result = board.shoot(2, 2)

    assert result == "hit"


def test_shoot_miss():
    board = Board()

    result = board.shoot(0, 0)

    assert result == "miss"


def test_shoot_already():
    board = Board()

    board.shoot(0, 0)

    result = board.shoot(0, 0)

    assert result == "already"


def test_remaining_ships():
    board = Board()

    board.place_ship(0, 0)
    board.place_ship(1, 1)

    assert board.remaining_ships() == 2


def test_remaining_ships_after_hit():
    board = Board()

    board.place_ship(0, 0)

    board.shoot(0, 0)

    assert board.remaining_ships() == 0