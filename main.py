from chess import WHITE, BLACK, STARTING_FEN
from ui import human_move, computer_move
from Board import Board

human = BLACK
depth = 6
book = True
starting_position = STARTING_FEN
print(f"Depth: {depth}, Book: {book}.")

board = Board(fen = starting_position)
end = board.is_game_over()
while not end:
    if human:
        end = human_move(board)
    else:
        try:
            backup = board.copy()
            end = computer_move(board, depth, book)
        except KeyboardInterrupt:
            print(" aborted by user.")
            board = backup
            board.pop()
    if human != "BOTH": human = not human
