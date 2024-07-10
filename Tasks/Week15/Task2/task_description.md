# Описание задачи

## Задача

Напишите программу, которая:
1. Запрашивает у пользователя его имя и сохраняет введенное значение в переменную `my_name`.
2. Запрашивает у пользователя год рождения и сохраняет в переменную `year_of_birth`.
3. Вычисляет возраст и сохраняет его в переменную с именем `age`.
4. Выводит на экран тип переменных `my_name`, `year_of_birth`, `age`.
5. Выводит сообщение "Hello my name is: my_name, My age: age".

## Пример использования

```python
from solution import greet_user

# Пример
my_name = "Alice"
year_of_birth = 1990
age = 2023 - year_of_birth

print("Тип переменной my_name:", type(my_name))
print("Тип переменной year_of_birth:", type(year_of_birth))
print("Тип переменной age:", type(age))

greet_user(my_name, age)
