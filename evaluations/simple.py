import chess

midGamePieceValue = {
    chess.PAWN   : 100,
    chess.KNIGHT : 320,
    chess.BISHOP : 330,
    chess.ROOK   : 500,
    chess.QUEEN  : 900,
    chess.KING   : 20000,
}
endGamePieceValue = midGamePieceValue

midGamePawnPosition = (
     0,  0,   0,   0,   0,   0,  0,  0,
    50, 50,  50,  50,  50,  50, 50, 50,
    10, 10,  20,  30,  30,  20, 10, 10,
     5,  5,  10,  25,  25,  10,  5,  5,
     0,  0,   0,  20,  20,   0,  0,  0,
     5, -5, -10,   0,   0, -10, -5,  5,
     5, 10,  10, -20, -20,  10, 10,  5,
     0,  0,   0,   0,   0,   0,  0,  0,
)
midGamePawnPositionWhite = tuple(reversed(midGamePawnPosition))
midGamePawnPositionBlack = tuple(reversed(midGamePawnPositionWhite))
endGamePawnPositionWhite = midGamePawnPositionWhite
endGamePawnPositionBlack = midGamePawnPositionBlack

midGameKnightPosition = (
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20,   0,   0,   0,   0, -20, -40,
    -30,   0,  10,  15,  15,  10,   0, -30,
    -30,   5,  15,  20,  20,  15,   5, -30,
    -30,   0,  15,  20,  20,  15,   0, -30,
    -30,   5,  10,  15,  15,  10,   5, -30,
    -40, -20,   0,   5,   5,   0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
)
midGameKnightPositionWhite = tuple(reversed(midGameKnightPosition))
midGameKnightPositionBlack = tuple(reversed(midGameKnightPositionWhite))
endGameKnightPositionWhite = midGameKnightPositionWhite
endGameKnightPositionBlack = midGameKnightPositionBlack

midGameBishopPosition = (
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -10,   0,   5,  10,  10,   5,   0, -10,
    -10,   5,   5,  10,  10,   5,   5, -10,
    -10,   0,  10,  10,  10,  10,   0, -10,
    -10,  10,  10,  10,  10,  10,  10, -10,
    -10,   5,   0,   0,   0,   0,   5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
)
midGameBishopPositionWhite = tuple(reversed(midGameBishopPosition))
midGameBishopPositionBlack = tuple(reversed(midGameBishopPositionWhite))
endGameBishopPositionWhite = midGameBishopPositionWhite
endGameBishopPositionBlack = midGameBishopPositionBlack

midGameRookPosition = (
     0,  0,  0,  0,  0,  0,  0,  0,
     5, 10, 10, 10, 10, 10, 10,  5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
     0,  0,  0,  5,  5,  0,  0,  0,
)
midGameRookPositionWhite = tuple(reversed(midGameRookPosition))
midGameRookPositionBlack = tuple(reversed(midGameRookPositionWhite))
endGameRookPositionWhite = midGameRookPositionWhite
endGameRookPositionBlack = midGameRookPositionBlack

midGameQueenPosition = (
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10,   0,   0,  0,  0,   0,   0, -10,
    -10,   0,   5,  5,  5,   5,   0, -10,
     -5,   0,   5,  5,  5,   5,   0, -5,
      0,   0,   5,  5,  5,   5,   0, -5,
    -10,   5,   5,  5,  5,   5,   0, -10,
    -10,   0,   5,  0,  0,   0,   0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20,
)
midGameQueenPositionWhite = tuple(reversed(midGameQueenPosition))
midGameQueenPositionBlack = tuple(reversed(midGameQueenPositionWhite))
endGameQueenPositionWhite = midGameQueenPositionWhite
endGameQueenPositionBlack = midGameQueenPositionBlack

midGameKingPosition = (
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
     20,  20,   0,   0,   0,   0,  20,  20,
     20,  30,  10,   0,   0,  10,  30,  20,
)
midGameKingPositionWhite = tuple(reversed(midGameKingPosition))
midGameKingPositionBlack = tuple(reversed(midGameKingPositionWhite))

endGameKingPosition = (
    -50, -40, -30, -20, -20, -30, -40, -50,
    -30, -20, -10,   0,   0, -10, -20, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -30,   0,   0,   0,   0, -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50,
)
endGameKingPositionWhite = tuple(reversed(endGameKingPosition))
endGameKingPositionBlack = tuple(reversed(endGameKingPositionWhite))

midGamePositionValue = {}
midGamePositionValue[chess.WHITE] = {
    chess.PAWN   : midGamePawnPositionWhite,
    chess.KNIGHT : midGameKnightPositionWhite,
    chess.BISHOP : midGameBishopPositionWhite,
    chess.ROOK   : midGameRookPositionWhite,
    chess.QUEEN  : midGameQueenPositionWhite,
    chess.KING   : midGameKingPositionWhite,
}
midGamePositionValue[chess.BLACK] = {
    chess.PAWN   : midGamePawnPositionBlack,
    chess.KNIGHT : midGameKnightPositionBlack,
    chess.BISHOP : midGameBishopPositionBlack,
    chess.ROOK   : midGameRookPositionBlack,
    chess.QUEEN  : midGameQueenPositionBlack,
    chess.KING   : midGameKingPositionBlack,
}

endGamePositionValue = {}
endGamePositionValue[chess.WHITE] = {
    chess.PAWN   : endGamePawnPositionWhite,
    chess.KNIGHT : endGameKnightPositionWhite,
    chess.BISHOP : endGameBishopPositionWhite,
    chess.ROOK   : endGameRookPositionWhite,
    chess.QUEEN  : endGameQueenPositionWhite,
    chess.KING   : endGameKingPositionWhite,
}
endGamePositionValue[chess.BLACK] = {
    chess.PAWN   : endGamePawnPositionBlack,
    chess.KNIGHT : endGameKnightPositionBlack,
    chess.BISHOP : endGameBishopPositionBlack,
    chess.ROOK   : endGameRookPositionBlack,
    chess.QUEEN  : endGameQueenPositionBlack,
    chess.KING   : endGameKingPositionBlack,
}
