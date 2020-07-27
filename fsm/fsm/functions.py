import math
from time import process_time


def convert_value(factor, start_value, temp_value):
    """ convert the value function """
    e = math.exp(-factor * process_time())
    result = temp_value + (start_value - temp_value) * e
    return result


def tick():
    """ create a function delay tick every 2 sec """
    start_time = process_time()
    while start_time + 2 > process_time():
        pass
