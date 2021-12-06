#!/usr/bin/env python3

import random

from game import Game

def main():
    game = Game()
    game.initGame()
    game.battleStart()
    game.main()

if __name__ == "__main__":
    main()
