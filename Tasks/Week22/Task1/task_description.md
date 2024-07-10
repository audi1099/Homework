# Описание задачи

## Задача

Реализовать генератор `random_colors`, который будет возвращать случайные цвета в формате RGB.

## Пример использования

```python
from solution import random_colors

gen = random_colors()

def main():
    print(next(gen))

if __name__ == "__main__":
    main()
