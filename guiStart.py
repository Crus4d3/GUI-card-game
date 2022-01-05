import pygame

from game import Game
from window import Window
from assets import Assets

def main():
    pygame.init()
    game = Game(Window(), Assets())
    game.mainMenu()

if __name__ == '__main__':
    main()
