# This file will contain the Connect4 class, which manages the board, moves, and game state


class Connect4:
    def __init__(self, rows=6, cols=7):
        """Initialize the game board and other game settings"""
        self.rows = 6
        self.cols = 7

        # Create a 6x7 board
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'

    def print_board(self):
        """Print the game board to the console."""
        print("\n")
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
        
        print('-' * (self.cols * 4 + 1))
        print('| '+' | '.join([str(i + 1) for i in range(self.cols)]) + ' |')
        print("\n")

    def is_valid_move(self, col):
        """Check if a move is valid (i.e., the column is not full)."""
        return self.board[0][col] == ' '

    def get_next_open_row(self, col):
        """Find the next available row in the selected column."""
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                return row

    def drop_piece(self, row, col, piece):
        """Place the player's piece in the chosen column."""
        self.board[row][col] = piece

    def check_win(self, piece):
        """Check for any winning sequence (horizontal, vertical, diagonal)."""
        # Check horizontal win
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if all(self.board[r][c + i] == piece for i in range(4)):
                    return True
        # Check vertical win
        for r in range(self.rows - 3):
            for c in range(self.cols):
                if all(self.board[r + i][c] == piece for i in range(4)):
                    return True
        # Check positively sloped diagonal win
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if all(self.board[r + i][c + i] == piece for i in range(4)):
                    return True
        # Check negatively sloped diagonal win
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if all(self.board[r - i][c + i] == piece for i in range(4)):
                    return True
        return False

    def board_is_full(self):
        """Check if the board is completely filled."""
        return all(self.board[0][col] != ' ' for col in range(self.cols))

    def valid_moves(self):
        """Return a list of valid column indices (where a move can be made in the board)."""
        return [col for col in range(self.cols) if self.is_valid_move(col)]

    def print_metrics(self, player):
        """Print performance metrics."""
        avg_move_time = (player.total_time / player.total_moves) * 1000
        
        print(f"\n")
        print(f"Average time for {player.name}: {avg_move_time:.4f} seconds")
