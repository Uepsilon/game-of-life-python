class Cell(object):
    """This are the Cells which can die or live """

    def __init__(self, init_state):
        super(Cell, self).__init__()

        self.current_state = init_state

    def kill(self):
        self.next_state = 0

    def reborn(self):
        self.next_state = 1

    def cycle(self):
        self.current_state = self.next_state

    def isAlive(self):
        return self.current_state is 1
