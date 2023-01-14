import sys

from game import Game

players = int(sys.argv[1])

print(f"Executing game with {players} players")
agame = Game(players)