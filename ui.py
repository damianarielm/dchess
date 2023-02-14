from time import time
from ai import choose_move
from evaluation import evaluate_board, legal_moves

def print_board(board, debug=True):
    print(f"\nBoard: {board.fen()}.\n", f"{board}", sep="\n")
    if debug:
        total, material, position, pawns, opening, columns = evaluate_board(board)
        print(f"\nMaterial evaluation: {material}.")
        print(f"Position evaluation: {position}.")
        print(f"Pawn evaluation:     {pawns}.")
        print(f"Opening evaluation:  {opening}.")
        print(f"Columns evaluation:  {columns}.")
        print(f"Static evaluation:   {total}.")

def human_move(board):
    move = None
    moves = tuple(map(board.san, legal_moves(board)))
    print_board(board)
    print("\nMoves:", *moves, "undo", "pass", "exit")
    while move not in moves:
        move = input("Enter a move: ")
        if move == "exit": return True
        if move == "pass":
            board.turn = not board.turn
            return False
        if move == "undo":
            board.pop()
            board.pop()
            return human_move(board)
    board.push_san(move)
    return board.is_game_over()

def computer_move(board, depth=6, book=True):
    print_board(board)
    moves = tuple(map(board.san, legal_moves(board)))
    print("\nMoves:", *moves)
    print("Thinking...", end="", flush=True)
    start = time()
    score, move, nodes = choose_move(board, depth, book)
    end = time()
    if move:
        print(f"{board.san(move)} ({int(end - start)} seconds).")
        print(f"Deep evaluation: {score} ({nodes} nodes explored).")
        if end - start:
            print(f"Evaluation speed: {int(nodes / (end - start))} n/s.")
        board.push(move)
        return board.is_game_over()
    else:
        print(f"Resign ({int(end - start)} seconds).")
        return True
