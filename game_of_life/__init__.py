# -*- coding: utf-8 -*-

"""Game of Life (Python)

Usage:
    game-of-life.py
    game-of-life.py --version

Options:
    -h --help           Show this screen.
    --version           Show version.

"""
from docopt import docopt
from world import World


def setupGame():
    # Well, here goes some code
    a_new_world = World()
    a_new_world.run()

if __name__ == '__main__':
    args = docopt(__doc__, version='Game of Life (Python): 0.1')
    setupGame(args)
