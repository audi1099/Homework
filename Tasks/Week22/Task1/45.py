# Создайте генератор, который будет возвращать случайные цвета в формате RGB
import random


def random_colors():
    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        yield r, g, b


gen = random_colors()
print(next(gen))
