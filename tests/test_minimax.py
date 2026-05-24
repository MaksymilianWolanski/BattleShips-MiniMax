from app.board import Board
from app.minimax import evaluate_move, minimax, minimax_ai_move


def test_evaluate_move_returns_int():
    board = Board()

    score = evaluate_move(board, 2, 2)

    assert isinstance(score, int)


def test_evaluate_move_prefers_center():
    board = Board()

    center_score = evaluate_move(board, 2, 2)
    corner_score = evaluate_move(board, 0, 0)

    assert center_score > corner_score


def test_evaluate_move_prefers_near_hit():
    board = Board()

    board.grid[2][2] = "X"

    near_score = evaluate_move(board, 2, 3)
    far_score = evaluate_move(board, 0, 0)

    assert near_score > far_score


def test_minimax_returns_int():
    board = Board()

    result = minimax(board, 1, True)

    assert isinstance(result, int)


def test_minimax_ai_move_returns_tuple():
    board = Board()

    move = minimax_ai_move(board)

    assert isinstance(move, tuple)
    assert len(move) == 2


def test_minimax_ai_move_not_used_field():
    board = Board()

    board.grid[0][0] = "O"

    move = minimax_ai_move(board)

    assert move != (0, 0)


def test_minimax_ai_move_prefers_adjacent():
    board = Board()

    board.grid[2][2] = "X"

    move = minimax_ai_move(board)

    valid_moves = [
        (1, 2),
        (3, 2),
        (2, 1),
        (2, 3),
    ]

    assert move in valid_moves