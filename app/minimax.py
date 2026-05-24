import random


BOARD_SIZE = 5


def evaluate_move(board, x, y):

    score = 0

    center_distance = abs(2 - x) + abs(2 - y)

    score += (4 - center_distance)

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dx, dy in directions:

        nx = x + dx
        ny = y + dy

        if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:

            if board.grid[nx][ny] == "X":
                score += 20

            if board.grid[nx][ny] == "O":
                score -= 3

    return score


def minimax(board, depth, maximizing_player):

    if depth == 0:
        return 0

    if maximizing_player:

        best_score = -9999

        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):

                if board.grid[i][j] in ["X", "O"]:
                    continue

                score = evaluate_move(board, i, j)

                best_score = max(best_score, score)

        return best_score

    else:

        best_score = 9999

        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):

                if board.grid[i][j] in ["X", "O"]:
                    continue

                score = evaluate_move(board, i, j)

                best_score = min(best_score, score)

        return best_score


def minimax_ai_move(board):

    best_score = -9999

    best_moves = []

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):

            if board.grid[i][j] in ["X", "O"]:
                continue

            score = evaluate_move(board, i, j)

            future_score = minimax(
                board,
                depth=1,
                maximizing_player=False
            )

            total_score = score + future_score

            if total_score > best_score:

                best_score = total_score
                best_moves = [(i, j)]

            elif total_score == best_score:

                best_moves.append((i, j))

    if not best_moves:

        while True:

            x = random.randint(0, BOARD_SIZE - 1)
            y = random.randint(0, BOARD_SIZE - 1)

            if board.grid[x][y] not in ["X", "O"]:
                return x, y

    return random.choice(best_moves)