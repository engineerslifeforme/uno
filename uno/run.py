import sys

from game import Game

players = int(sys.argv[1])
a_game = Game(players)
a_game.play()