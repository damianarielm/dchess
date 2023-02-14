import chess
from evaluations.simple import midGamePositionValue, endGamePositionValue, \
                               midGamePieceValue, endGamePieceValue

infinity = 100000000

center = chess.SquareSet(chess.BB_CENTER)
big_center = chess.SquareSet(chess.BB_C6 | chess.BB_D6 | chess.BB_E6 |
                             chess.BB_F6 | chess.BB_C5 | chess.BB_F5 |
                             chess.BB_C4 | chess.BB_F4 | chess.BB_C3 |
                             chess.BB_D3 | chess.BB_E3 | chess.BB_F3)

def evaluate_capture(board, move, pieceValue):
    victim = board.piece_type_at(move.to_square)
    aggressor = board.piece_type_at(move.from_square)
    return pieceValue[victim] - pieceValue[aggressor]

def evaluate_move(board, move):
    total = 0

    if board.is_castling(move):
      total += 2
    else:
        pieceValue = endGamePieceValue if board.is_end_game() else midGamePieceValue
        to_square = move.to_square
        if board.is_en_passant(move):
          total += pieceValue[chess.PAWN]
        elif board.piece_at(to_square): # Capture bugfix
          total += infinity + evaluate_capture(board, move, pieceValue)
        if to_square in center:
          total += 2
        elif to_square in big_center:
          total += 1

    return total

def legal_moves(board):
    moves = board.legal_moves
    return sorted(moves, key=lambda m: evaluate_move(board, m), reverse=True)

def evaluate_board(board):
    if board.is_checkmate():
        return (infinity,0,0,0,0) if board.outcome().winner else (-infinity,0,0,0,0)

    white_pawns = set()
    black_pawns = set()
    is_end_game = board.is_end_game()
    is_opening = board.is_opening()
    positionValue = endGamePositionValue if is_end_game else midGamePositionValue
    pieceValue = endGamePieceValue if is_end_game else midGamePieceValue
    opening_penalization = pieceValue[chess.PAWN] // 4
    doubled_pawns_penalization = pieceValue[chess.PAWN] // 3
    passed_pawns_bonification = pieceValue[chess.PAWN] // 3
    isolated_pawns_penalization = pieceValue[chess.PAWN] // 3
    open_columns_penalization = pieceValue[chess.PAWN] // 3
    position = material = pawns = columns = opening = 0
    for square, piece in board.piece_map().items():
        piece_type = piece.piece_type
        color = piece.color

        # evaluate position
        value = positionValue[color][piece_type][square]
        position += value if color else -value
        # evaluate material
        value = pieceValue[piece_type]
        material += value if color else -value
        # evaluate doubled pawns
        if piece_type == chess.PAWN:
            file = chess.square_file(square)
            if color:
                if file in white_pawns:
                    pawns -= doubled_pawns_penalization
                else:
                    white_pawns.add(file)
            else:
                if file in black_pawns:
                    pawns += doubled_pawns_penalization
                else:
                    black_pawns.add(file)
        # evaluate open columns against king
        elif piece_type == chess.KING:
            file = chess.square_file(square)
            if color:
                white_king_file = file
            else:
                black_king_file = file
        # evaluate opening
        elif is_opening and piece_type != chess.ROOK:
            rank = chess.square_rank(square)
            if color:
                if piece_type == chess.KNIGHT and square in (chess.B1, chess.G1):
                    opening -= opening_penalization
                elif piece_type == chess.BISHOP and square in (chess.C1, chess.F1):
                    opening -= opening_penalization
                elif piece_type == chess.QUEEN and rank > 2:
                    opening -= opening_penalization
            else:
                if piece_type == chess.KNIGHT and square in (chess.B8, chess.G8):
                    opening += opening_penalization
                elif piece_type == chess.BISHOP and square in (chess.C8, chess.F8):
                    opening += opening_penalization
                elif piece_type == chess.QUEEN and rank < 5:
                    opening += opening_penalization

    if chess.Move(chess.E1, chess.G1) not in board.move_stack and \
       chess.Move(chess.E1, chess.C1) not in board.move_stack:
           opening -= opening_penalization * 2
    if chess.Move(chess.E8, chess.G8) not in board.move_stack and \
       chess.Move(chess.E8, chess.C8) not in board.move_stack:
           opening += opening_penalization * 2

    # evaluate passed and isolated pawns
    for file in white_pawns:
        if file not in black_pawns and file-1 not in black_pawns and file+1 not in black_pawns:
            pawns += passed_pawns_bonification
        if file-1 not in white_pawns and file+1 not in white_pawns:
            pawns -= isolated_pawns_penalization
    for file in black_pawns:
        if file not in white_pawns and file-1 not in white_pawns and file+1 not in white_pawns:
            pawns -= passed_pawns_bonification
        if file-1 not in black_pawns and file+1 not in black_pawns:
            pawns += isolated_pawns_penalization
    # evaluate open columns against king
    for file in (white_king_file, white_king_file-1, white_king_file+1):
        if file not in black_pawns:
            columns -= open_columns_penalization
        if file not in white_pawns:
            columns -= open_columns_penalization
    for file in (black_king_file, black_king_file-1, black_king_file+1):
        if file not in white_pawns:
            columns += open_columns_penalization
        if file not in black_pawns:
            columns += open_columns_penalization

    total = material + position + pawns + opening + columns
    return total, material, position, pawns, opening, columns
