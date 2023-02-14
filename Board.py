import chess
from chess.polyglot import zobrist_hash

class Board(chess.Board):
    __hash__ = zobrist_hash

    def is_opening(self):
        return len(self.move_stack) <= 10 * 2

    def is_end_game(self):
        queens  = len(self.pieces(chess.QUEEN, chess.WHITE))
        queens += len(self.pieces(chess.QUEEN, chess.BLACK))
        minors  = len(self.pieces(chess.BISHOP, chess.WHITE))
        minors += len(self.pieces(chess.BISHOP, chess.BLACK))
        minors += len(self.pieces(chess.KNIGHT, chess.WHITE))
        minors += len(self.pieces(chess.KNIGHT, chess.BLACK))

        return queens == 0 or (queens == 2 and minors <= 1)

    def __str__(self, white=True):
        rows = self.unicode(invert_color=True, empty_square="·", orientation = white)
        rows = rows.split("\n")

        if white:
            rows = [f"{9-n} {row}" for n, row in zip(range(1, 9), rows)]
            rows.append("  a b c d e f g h")
        else:
            rows = [f"{n} {row}" for n, row in zip(range(1, 9), rows)]
            rows.append("  h g f e d c b a")

        return "\n".join(rows)
