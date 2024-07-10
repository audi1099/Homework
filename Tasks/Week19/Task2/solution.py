import random

def random_number_generator(start, end):
    while True:
        yield random.randint(start, end)
