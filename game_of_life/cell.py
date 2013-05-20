class Cell(object):
    """This are the Cells which can die or live """

    def __init__(self, init_state, pos_x, pos_y):
        super(Cell, self).__init__()

        self.next_state = init_state
        self.pos_x = pos_x
        self.pos_y = pos_y

    def kill(self):
        self.next_state = 0

    def reborn(self):
        self.next_state = 1

    def cycle(self):
        self.current_state = self.next_state

    def isAlive(self):
        return self.current_state is 1

    def isDead(self):
        return self.current_state is not 1

    def getPosX(self):
        return self.pos_x

    def getPosY(self):
        return self.pos_y
