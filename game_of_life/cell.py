class Cell(object):
    """This are the Cells which can die or live """

    def __init__(self, init_state, pos_x, pos_y):
        super(Cell, self).__init__()

        self.current_state = init_state
        self.alive_neighbors = 3 if init_state is 1 else 0
        self.pos_x = pos_x
        self.pos_y = pos_y

    def cycle(self):
        changed = False

        if self.isAlive():
            if self.alive_neighbors is not 2 and self.alive_neighbors is not 3:
                self.current_state = 0
                changed = True
        else:
            if self.alive_neighbors is 3:
                self.current_state = 1
                changed = True

        self.alive_neighbors = 0

        return changed

    def addNeighbor(self):
        self.alive_neighbors += 1

    def isAlive(self):
        return self.current_state is 1
