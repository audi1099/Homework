# Описание задачи

## Задача

Создать словарь студенческих билетов, в котором ключом является номер студенческого билета (трехзначное число от 0 до 999), а значением - строка с именем и фамилией студента.

## Реализация

### Файл solution.py

```python
import random

def create_student_dict():
    student_dict = {}
    used_tickets = set()

    while len(student_dict) < 10:
        ticket_number = random.randint(0, 999)
        if ticket_number not in used_tickets:
            used_tickets.add(ticket_number)
            name = input(f"Введите имя и фамилию для студенческого билета №{ticket_number}: ")
            student_dict[ticket_number] = name
        else:
            continue

    return student_dict

# Для тестирования функции в solution.py:
if __name__ == "__main__":
    students = create_student_dict()
    print(students)
