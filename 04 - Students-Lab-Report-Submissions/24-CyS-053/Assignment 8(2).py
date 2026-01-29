import math

PLAYER = 'X'
OPPONENT = 'O'


def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False


def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return 10 if board[i][0] == PLAYER else -10

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return 10 if board[0][i] == PLAYER else -10

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return 10 if board[0][0] == PLAYER else -10

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return 10 if board[0][2] == PLAYER else -10

    return 0


def minimax(board, is_max):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    best = max(best, minimax(board, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = OPPONENT
                    best = min(best, minimax(board, True))
                    board[i][j] = ' '
        return best


board = [
    ['O', 'X', 'O'],
    ['O', 'X', 'X'],
    ['X', 'O', 'X']
]

print("Minimax evaluation:", minimax(board, True))
