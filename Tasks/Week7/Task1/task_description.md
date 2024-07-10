# Описание задачи

## Задача

Написать функцию, которая принимает список словарей, где каждый словарь представляет собой запись об ученике (с ключами 'имя', 'возраст', 'оценки'), и возвращает список словарей, отсортированный по возрасту учеников в порядке убывания.

## Пример использования

```python
from solution import sort_by_age

students = [
    {"name": "John", "age": 25, "ratings": [5, 3, 5, 4, 4, 3, 5]},
    {"name": "Vitaliy", "age": 41, "ratings": [5, 4, 5, 4, 4, 4, 5]},
    {"name": "Vlad", "age": 19, "ratings": [5, 4, 5, 4, 4, 5, 5]},
    {"name": "Oleg", "age": 29, "ratings": [5, 5, 5, 3, 4, 3, 5]},
]

sorted_students = sort_by_age(students)
for student in sorted_students:
    print(f"Имя: {student['name']}, Возраст: {student['age']}, Оценки: {student['ratings']}")
