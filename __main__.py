#!/usr/bin/env python3

import argparse

from textGame import Game

def parseArgs():
    parser = argparse.ArgumentParser(description='Process command line arguments')
    parser.add_argument('--version', action='store_true', help='output version information and exit')
    parser.add_argument('-t', '--text', action='store_true', help='run in text mode only')
    parser.add_argument('-g', '--gui', action='store_true', help='run in graphical mode')
    return parser.parse_args()

def loadGame(args):
    def version():
        print("Version {}".format('0.3.0'))
        print("This project is still in active development")
        print("Visit https://github.com/crus4d3/gui-card-game for the latest version")
        quit()

    def text():
        game = Game()
        game.initGame()
        game.battleStart()
        game.main()

    def gui():
        try:
            import pygame
            from guiGame import Game
            from window import Window
            from assets import Assets
            guiGameStart()
        except ImportError:
            print("Error could not import gui mode, running in text mode \n")
            try:
                text()
            except NameError:
                print("Fatal error no game found \n")
                print("You have really messed things up haven't you >:(")

        def guiGameStart():
            pygame.init()
            game = Game(Window(), Assets())
            game.mainMenu()

    if args.version:
        version()
    if args.text:
        text()
    if args.gui:
        gui()
    else:
        gui()

def main():
    args = parseArgs()
    loadGame(args)

if __name__ == "__main__":
    main()
