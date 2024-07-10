# Создайте генератор, который будет возвращать случайные числа в заданном диапазоне.
import random


def ran_numbers():
    for i in range(0, 10):
        yield random.randint(0, 10)


for number in ran_numbers():
    print(number)
