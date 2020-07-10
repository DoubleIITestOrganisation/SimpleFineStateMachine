

class Transition(object):
    """ transition to next state """
    def __init__(self, to_state):
        self.to_state = to_state

    def execute(self):
        print('Transitioning to state ...')
