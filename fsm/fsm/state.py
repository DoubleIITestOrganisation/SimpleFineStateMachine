import math
from time import process_time


def convert_value(factor, start_value, temp_value):
    """ convert the value function """
    e = math.exp(-factor * process_time())
    result = temp_value + (start_value - temp_value) * e
    return result


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
