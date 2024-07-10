# Описание задачи

## Задача

Написать функцию, принимающую число и возвращающую следующий за этим числом палиндром.

## Пример использования

```python
from solution import palindrome

input_number = int(input("Введите число: "))
result = palindrome(input_number)
print(f"Следующий палиндром после числа {input_number} : {result}")
