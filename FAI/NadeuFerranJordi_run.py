# This file will handle the main game loop, allowing the user to select game modes and start the game

import time
from connect4 import Connect4
from players import HumanPlayer, RandomBot, GreedyBestFirstSearchBot, MinimaxBot

def play_game(game_mode='bot_vs_bot', ai_difficulty='easy'):
    """Play the game in either bot-vs-bot or human-vs-bot mode."""
    game = Connect4()

    # Init players
    player1 = player2 = None
    
    if game_mode == 'human_vs_bot':
        player1 = HumanPlayer(game, 'X')
        if ai_difficulty == 'hard':
            bot = MinimaxBot(game, 'O', depth=4)
        elif ai_difficulty == 'medium':
            bot = GreedyBestFirstSearchBot(game, 'O', player1)
        else:
            bot = RandomBot(game, 'O')

        player2 = bot

    else:
        player1 = RandomBot(game, 'X')
        player2 = GreedyBestFirstSearchBot(game, 'O', player1) 

    current_player = player1

    while True:
        game.print_board()
        if isinstance(current_player, HumanPlayer):
            print(f"Human's turn ({current_player.piece})")
        else:
            print(f"{current_player.name} ({current_player.piece}) is thinking...")

        # Current player makes a move
        col = current_player.choose_move()
        row = game.get_next_open_row(col)
        game.drop_piece(row, col, current_player.piece)

        # Check for win
        if game.check_win(current_player.piece):
            game.print_board()
            print(f"-----------Game finished!-----------")
            print(f"Player {current_player.name} ({current_player.piece}) wins!")
            #game.print_metrics(player1)
            #game.print_metrics(player2)
            break

        # Check for draw
        if game.board_is_full():
            game.print_board()
            print(f"Game finished!")
            print("It's a draw!")
            #game.print_metrics(player1)
            #game.print_metrics(player2)
            break

        # Switch players
        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    print("-----------Welcome to Connect 4!-----------")
    print("Select game mode:")
    print("1: Bot vs Bot")
    print("2: Human vs Bot")
    game_mode = input("Enter your choice (1 or 2): ")

    if game_mode == '2':
        print("Select AI difficulty:")
        print("1: Easy (Random Bot)")
        print("2: Medium (GBFS Bot)")
        print("3: Hard (Minimax Bot)")
        difficulty = input("Enter your choice (1, 2 or 3): ")
        if difficulty == '3':
            play_game(game_mode='human_vs_bot', ai_difficulty='hard')
        elif difficulty == '2':
            play_game(game_mode='human_vs_bot', ai_difficulty='medium')
        else:
            play_game(game_mode='human_vs_bot', ai_difficulty='easy')

    else:
        play_game(game_mode='bot_vs_bot')
