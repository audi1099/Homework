# Описание задачи

## Задача

Напишите программу, которая проверяет, является ли введенное пользователем число четным.

## Пример использования

```python
from solution import check_even_odd

number = int(input("Введите число: "))

if check_even_odd(number):
    print("Число четное")
else:
    print("Число нечетное")
