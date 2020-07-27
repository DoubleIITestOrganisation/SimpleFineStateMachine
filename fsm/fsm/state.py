

class State(object):
    """ base state class """
    def __init__(self, fsm):
        self.fsm = fsm

    def enter(self):
        print('State enter')

    def execute(self):
        pass

    def exit(self):
        pass
