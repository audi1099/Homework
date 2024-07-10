import random

def random_numbers(start, end):
    while True:
        yield random.randint(start, end)
