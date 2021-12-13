#!/usr/bin/env python3

import argparse

from game import Game

def parseArgs():
    parser = argparse.ArgumentParser(description='Process command arguments')
    parser.add_argument('--text', help='runs the game in text mode only')
    args = parser.parse_args()

def main():
    parseArgs()
    game = Game()
    game.initGame()
    game.battleStart()
    game.main()

if __name__ == "__main__":
    main()
