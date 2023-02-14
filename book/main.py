from .open import main as open
from .closed import main as closed
from .semiopen import main as semiopen
from .semiclosed import main as semiclosed
from .others import main as others

book = {}

# Starting position
book["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"] = "e4"

# e4
book["rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"] = "c5"
# d4
book["rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1"] = "Nf6"

book |= open.book
book |= closed.book
book |= semiopen.book
book |= semiclosed.book
book |= others.book
