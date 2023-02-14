from evaluation import evaluate_board, infinity, legal_moves
from book.main import book

def negamax(board, depth, alpha, beta, isMaximizing):
    if depth <= 0 or board.is_game_over():
        total, *_ = evaluate_board(board)
        return total * (1 if isMaximizing else -1), board.peek(), 1

    bestValue = -infinity
    bestMove = None
    nodes = 0
    for move in legal_moves(board):
        board.push(move)
        value, _, nodes_ = negamax(board, depth-1, -beta, -alpha, not isMaximizing)
        value = -value
        nodes += nodes_
        board.pop()

        if value > bestValue:
            bestValue, bestMove = value, move

        alpha = max(alpha, bestValue)
        if alpha >= beta: break

    return bestValue, bestMove, nodes

def choose_move(board, depth=6, opening_book=True):
    if opening_book and board.fen() in book:
        return "Book", board.parse_san(book[board.fen()]), 0

    return negamax(board, depth, -infinity, infinity, board.turn)
