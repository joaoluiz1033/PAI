from pypgn.game import Game
# Importing game from file on disk
chess_game = Game('test.pgn')

# Import game from Lichess
chess_game.pgn('dGm3ND39')

print(chess_game.tag('Event'))
print(chess_game.result())
# Print opening ply for white
print(chess_game.ply(1, 'w'))