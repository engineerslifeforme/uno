import sys

from auto_uno.game import Game

def main():
    players = int(sys.argv[1])
    a_game = Game(players)
    a_game.play()

if __name__ == "__main__":
    main()