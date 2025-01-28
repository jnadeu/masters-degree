# This file contains utility functions (such as board evaluation)

import numpy as np

def make_move(board, col, player):
    """Make a move on the board."""
    for row in reversed(range(board.shape[0])):  # Start from the bottom
        if board[row, col] == ' ':
            board[row, col] = player
            break
    return board

def evaluate_board(board, player):
    """Evaluate the board and return a score for the given player."""
    score = 0
    opponent = 'X' if player == 'O' else 'O'

    # Check horizontal
    for r in range(board.shape[0]):
        for c in range(board.shape[1] - 3):
            window = board[r, c:c + 4]
            score += evaluate_window(window, player, opponent)

    # Check vertical
    for c in range(board.shape[1]):
        for r in range(board.shape[0] - 3):
            window = board[r:r + 4, c]
            score += evaluate_window(window, player, opponent)

    # Check diagonal (positive slope)
    for r in range(3, board.shape[0]):
        for c in range(board.shape[1] - 3):
            window = [board[r - i, c + i] for i in range(4)]
            score += evaluate_window(window, player, opponent)

    # Check diagonal (negative slope)
    for r in range(board.shape[0] - 3):
        for c in range(board.shape[1] - 3):
            window = [board[r + i, c + i] for i in range(4)]
            score += evaluate_window(window, player, opponent)

    return score

def evaluate_window(window, player, opponent):
    """Evaluate a window (4 positions) and return a score."""
    score = 0
    if np.count_nonzero(window == player) == 4:
        score += 100  # Win for player
    elif np.count_nonzero(window == opponent) == 4:
        score -= 100  # Win for opponent
    elif np.count_nonzero(window == player) == 3 and np.count_nonzero(window == ' ') == 1:
        score += 5  # Potential threat for player
    elif np.count_nonzero(window == opponent) == 3 and np.count_nonzero(window == ' ') == 1:
        score -= 5  # Potential threat for opponent

    return score