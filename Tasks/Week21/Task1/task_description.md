# Описание задачи

## Задача

Реализовать декоратор, который добавляет задержку перед выполнением функции.

## Пример использования

```python
from solution import delay_decorator

@delay_decorator(4)
def example_function(x, y):
    result = x / y
    print("Result:", result)

def main():
    example_function(10, 2)

if __name__ == "__main__":
    main()
