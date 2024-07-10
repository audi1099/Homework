# Описание задачи

## Задача

Напишите программу, которая определяет наибольшее и наименьшее из двух чисел, введенных пользователем.

## Пример использования

```python
from solution import find_min_max

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

min_number, max_number = find_min_max(number_1, number_2)

print("Наибольшее число: ", max_number)
print("Наименьшее число: ", min_number)
