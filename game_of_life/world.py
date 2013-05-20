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
    width = 30
    height = 30
    fill_percentage = 25
    idle = 1000
    borders = True
    cycle_delay = 100

    def __init__(self):
        super(World, self).__init__()

        # feeling like the constructor of the matrix
        self.populateWorld()

    def run(self):
        cycles = 0

        print "Starting a new Game! Width: " + str(self.width)\
            + " | Height: " + str(self.height)\
            + " | Initial Percantage: " + str(self.fill_percentage) + "%"

        while (cycles is 0) or self.cycle():
            os.system('clear')
            print "Cycle #" + str(cycles)
            # only working on unix based OS
            self.showWorld()
            cycles += 1

            time.sleep(self.cycle_delay / 1000)

        raw_input('Game endet...')

    def populateWorld(self):
        cellCount = self.width * self.height
        aliveCells = cellCount * self.fill_percentage / 100
        aliveChance = aliveCells / cellCount

        self.game_field = [[[] for column in range(self.width)] for row in range(self.height)]

        for row in range(self.height):
            for cell in range(self.width):
                state = 1 if (random() <= aliveChance) else 0
                self.game_field[row][cell] = Cell(state, row, cell)

    def showWorld(self):
        for row in self.game_field:
            print '|',
            for cell in row:
                cell.cycle()
                print (self.alive_marker if cell.isAlive() else self.dead_marker),
            print '|'

    def cycle(self):
        changed = False

        for row in self.game_field:
            for cell in row:
                changed = self.checkCell(cell) or changed

        return changed

    def checkCell(self, cell):
        aliveNeighbors = 0


        # needs 2 + 3 to stay alive
        for x in range(-1, 2):
            row = cell.getPosX() + x

            # check wether the used row is in the grid or not
            if self.borders is True:
                if row < 0 or row >= self.height:
                    # row out of bounce
                    continue
            else:
                # caluclate row values if borders are not used
                if row > self.height:
                    row = row - self.height
                elif row < 0:
                    row = self.height - row

            for y in range(-1, 2):
                column = cell.getPosY() + y

                # check if new coords are in grid
                if self.borders is True:
                    if column < 0 or column >= self.width:
                        # column out of bounce
                        continue
                else:
                    # calculate column values if borders are not used
                    if column > self.width:
                        column = column - self.width
                    elif column < 0:
                        column = self.width - column

                if self.game_field[row][column].isAlive() and \
                   self.game_field[row][column] is not cell:
                    aliveNeighbors += 1

                # raw_input('waiting...')

        if cell.isAlive():
            if aliveNeighbors is not 2 and aliveNeighbors is not 3:
                cell.kill()
                return 1
        else:
            if aliveNeighbors is 3:
                cell.reborn()
                return 1

        return 0
