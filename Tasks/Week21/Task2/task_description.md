# Описание задачи

## Задача

Реализовать декоратор `upper_decorator`, который преобразует результат выполнения функции в верхний регистр.

## Пример использования

```python
from solution import upper_decorator

@upper_decorator
def greet():
    return "redrdyy, dfdhgfh gjhgjhkjh vjghi"

def main():
    print(greet())

if __name__ == "__main__":
    main()
