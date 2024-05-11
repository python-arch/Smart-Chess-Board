import chess
import chess.engine
import random

def board_array_to_fen(board_array):
    fen = ''
    for row in board_array:
        empty_count = 0
        for piece in row:
            if piece == '.':
                empty_count += 1
            else:
                if empty_count > 0:
                    fen += str(empty_count)
                    empty_count = 0
                fen += piece
        if empty_count > 0:
            fen += str(empty_count)
        fen += '/'
    fen = fen[:-1]
    return fen

def simulate_game(difficulty):
    board_array = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]

    board = chess.Board()

    # Set the board position from the 2D array
    fen = board_array_to_fen(board_array)
    board.set_fen(fen)

    # Simulate the game
    while not board.is_game_over():
        # White=== rasberry , Black == user
        player_color = 'White' if board.turn == chess.WHITE else 'Black'

        # Make a move for the current player
        if player_color == 'White':
            if difficulty == 'easy':
                move = random.choice(list(board.legal_moves))
            elif difficulty == 'medium':
                sorted_moves = sorted(list(board.legal_moves), key=lambda move: board.san(move))
                move = random.choice(sorted_moves[:len(sorted_moves)//2])
            else:   
                    engine = chess.engine.SimpleEngine.popen_uci(r"")
                    result = engine.play(board, chess.engine.Limit(time=0.1))
                    move = result.move
        else:
            print("Current board:")
            print(board)
            # Player move
            valid_move = False
            while not valid_move:
                player_move = input("Enter your move in SAN format (e.g., e2e4): ")
                try:
                    move = chess.Move.from_uci(player_move)
                    if move in board.legal_moves:
                        valid_move = True
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid move format. Try again.")

        board.push(move)

        print(f"{player_color} moves: {move}")
        print(board)

    print("Game over. Result:", board.result())

simulate_game('hard')
