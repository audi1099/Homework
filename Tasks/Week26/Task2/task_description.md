# Описание задачи

## Задача

Напишите генератор, который будет возвращать только четные числа из заданного диапазона.

## Генератор в solution.py

### Генератор even_number_generator

```python
def even_number_generator(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            yield i
