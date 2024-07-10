# Создайте генератор, который будет возвращать случайные числа в заданном диапазоне
import random


def random_numbers(start, end):
    while True:
        yield random.randint(start, end)


gen = random_numbers(1, 100)
print(next(gen))
