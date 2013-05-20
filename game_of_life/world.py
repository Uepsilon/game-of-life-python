from __future__ import division
from cell import Cell
from random import random
import os
import time

class World(object):
    """The World describes the Field of the Game. """

    game_field = [[]]
    alive_marker = '#'
    dead_marker = ' '
    width = 75
    height = 50
    fill_percentage = 25
    borders = False
    cycle_delay = 50

    def __init__(self):
        super(World, self).__init__()

        # feeling like the constructor of the matrix
        self.populateWorld()

    def run(self):
        cycles = 0
        changed = False

        print "Starting a new Game! Width: " + str(self.width)\
            + " | Height: " + str(self.height)\
            + " | Initial Percantage: " + str(self.fill_percentage) + "%"

        while (cycles is 0) or changed:
            os.system('clear')
            print "Cycle #" + str(cycles + 1)
            # only working on unix based OS
            self.cycle()
            changed = self.showWorld()
            cycles += 1

            time.sleep(self.cycle_delay / 1000)

        raw_input('Game endet...')


    def populateWorld(self):
        cellCount = self.width * self.height
        aliveCells = cellCount * self.fill_percentage / 100
        aliveChance = aliveCells / cellCount

        self.game_field = [
            [
                Cell(1, row, column) if (random() <= aliveChance) else Cell(0, row, column)
                for column in range(self.width)]
            for row in range(self.height)]

    def showWorld(self):
        changed = False

        for row in self.game_field:
            print '|',
            for cell in row:
                changed = cell.cycle() or changed
                print (self.alive_marker if cell.isAlive() else self.dead_marker),
            print '|'

        return changed

    def cycle(self):
        for row in self.game_field:
            for cell in row:
                self.checkCell(cell)

    def checkCell(self, cell):
        if cell.isAlive():
            for row in range(cell.pos_x - 1, cell.pos_x + 2):
                if self.borders is True:
                    if row < 0 or row >= self.height:
                        continue
                else:
                    row = row % self.height

                for column in range(cell.pos_y - 1, cell.pos_y + 2):
                    if self.borders is True:
                        if column < 0 or column >= self.width:
                            continue
                    else:
                        column = column % self.width

                    if self.game_field[row][column] is not cell:
                        self.game_field[row][column].addNeighbor()
