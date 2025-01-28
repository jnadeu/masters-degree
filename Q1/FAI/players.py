# This file will contain the logic for different players Classes

import random
import time
import numpy as np
from connect4 import Connect4
from utils import make_move, evaluate_board


class RandomBot:
    """Random AI bot - Chooses a random valid move."""
    def __init__(self, game, piece):
        """Initialize the random bot with the game and its piece."""
        self.name = "Random Bot"
        self.game = game
        self.piece = piece
        self.total_moves = 0
        self.total_time = 0

    def choose_move(self):
        """Select a random column for the move."""
        # Start timing the move
        start_time = time.time()

        col = random.choice(self.game.valid_moves())
        print(f"Random Bot chose column {col + 1}")

        # Calculate the time taken for the move
        end_time = time.time()
        # Add the move time to total time
        self.total_time += (end_time - start_time)

        # Increment total moves count
        self.total_moves += 1

        return col


class GreedyBestFirstSearchBot:
    """ GBFS AI Bot that makes the move that leads to the most immediate benefit."""
    def __init__(self, game, piece, player):
        self.name = "GBFS Bot"
        self.game = game
        self.player = player
        self.piece = piece
        self.total_moves = 0
        self.total_time = 0

    def choose_move(self):
        """Choose the best column using Greedy Best-First Search."""
        # Start timing the move
        start_time = time.time()

        valid_moves = self.game.valid_moves()
        best_col = None
        best_h_value = float('-inf')

        for col in valid_moves:
            # Simulate the move
            temp_board = make_move(np.copy(self.game.board), col, self.player)
            h_value = evaluate_board(temp_board, self.player)

            # Choose the column with the highest heuristic value
            if h_value > best_h_value:
                best_h_value = h_value
                best_col = col
        print(f"GBFS Bot chose column {best_col}")

        # Calculate the time taken for the move
        end_time = time.time()
        # Add the move time to total time
        self.total_time += (end_time - start_time)

        # Increment total moves count
        self.total_moves += 1

        return best_col


class MinimaxBot:
    """ Minimax AI Bot with depth-limited search."""
    def __init__(self, game, piece, depth=3):
        """Initialize the minimax bot with game, piece, and search depth."""
        self.name = "Minimax Bot"
        self.game = game
        self.piece = piece
        self.opponent_piece = 'O' if piece == 'X' else 'X'
        self.depth = depth
        self.total_moves = 0
        self.total_time = 0

    def score_position(self, piece):
        """Evaluate the current board state for a given piece (heuristic)."""
        if self.game.check_win(piece):
            return 1000
        elif self.game.check_win(self.opponent_piece):
            return -1000
        return 0

    def minimax(self, depth, alpha, beta, maximizing_player):
        """The minimax algorithm with depth-limited search and basic evaluation."""
        valid_moves = self.game.valid_moves()

        if depth == 0 or self.game.board_is_full():
            return None, self.score_position(self.piece)

        if maximizing_player:
            best_score = -float('inf')
            best_col = random.choice(valid_moves)
            for col in valid_moves:
                row = self.game.get_next_open_row(col)
                self.game.drop_piece(row, col, self.piece)
                _, score = self.minimax(depth - 1, alpha, beta, False)
                self.game.board[row][col] = ' '  # Undo the move
                if score > best_score:
                    best_score = score
                    best_col = col
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
            return best_col, best_score
        else:
            best_score = float('inf')
            best_col = random.choice(valid_moves)
            for col in valid_moves:
                row = self.game.get_next_open_row(col)
                self.game.drop_piece(row, col, self.opponent_piece)
                _, score = self.minimax(depth - 1, alpha, beta, True)
                self.game.board[row][col] = ' '  # Undo the move
                if score < best_score:
                    best_score = score
                    best_col = col
                beta = min(beta, score)
                if alpha >= beta:
                    break
            return best_col, best_score

    def choose_move(self):
        """Choose the best move using the minimax algorithm."""
        # Start timing the move
        start_time = time.time()
        best_col, _ = self.minimax(self.depth, -float('inf'), float('inf'), True)
        print(f"Minimax Bot chose column {best_col + 1}")

        # Calculate the time taken for the move
        end_time = time.time()
        # Add the move time to total time
        self.total_time += (end_time - start_time)

        # Increment total moves count
        self.total_moves += 1

        return best_col



class HumanPlayer:
    """Human player - Allows a human player to input a move"""
    def __init__(self, game, piece):
        """Initialize the human player with the game and their piece."""
        self.name = "Human"
        self.game = game
        self.piece = piece

    def choose_move(self):
        """Prompt the user to input a column for the move."""
        valid_move = False
        while not valid_move:
            try:
                col = int(input("Enter the column (1-7): ")) - 1
                if col >= 0 and col < self.game.cols and self.game.is_valid_move(col):
                    valid_move = True
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 7.")
        return col