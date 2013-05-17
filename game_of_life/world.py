from __future__ import division
from cell import Cell
from random import random

class World(object):
    """The World describes the Field of the Game. """

    game_field = [[]]
    alive_marker = '#'
    dead_marker = ' '
    width = 30
    height = 30
    fill_percentage = 10

    def __init__(self, width=None, height=None, fill_percentage=None):
        super(World, self).__init__()

        if not width is None:
            self.width = width

        if not height is None:
            self.height = height

        if not fill_percentage is None:
            self.fill_percentage = fill_percentage

        # feeling like the constructor of the matrix
        self.populateWorld()

    def run(self):
        print "Starting a new Game! Width: " + str(self.width)\
            + " | Height: " + str(self.height)\
            + " | Initial Percantage: " + str(self.fill_percentage)
        self.showWorld()

    def populateWorld(self):
        cellCount = self.width * self.height
        aliveCells = cellCount * self.fill_percentage / 100
        aliveChance = aliveCells / cellCount

        self.game_field = [[[] for column in range(self.height)] for row in range(self.width)]

        for row in range(self.width):
            for cell in range(self.height):
                state = 1 if (random() <= aliveChance) else 0
                self.game_field[row][cell] = Cell(state)

    def showWorld(self):
        for row in self.game_field:
            print '|',
            for cell in row:
                print (self.alive_marker if cell.isAlive() else self.dead_marker),
            print '|'

