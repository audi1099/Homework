# Описание задачи

## Задача

Пользователь вводит два положительных числа X и R, где X < R. Необходимо использовать цикл while для вывода на экран всех чисел в промежутке от X до R включительно, а также подсчитать их количество.

## Решение в solution.py

### Функция print_and_count_numbers

```python
def print_and_count_numbers(x, r):
    count = 0
    while x <= r:
        print(x)
        x += 1
        count += 1
    return count
