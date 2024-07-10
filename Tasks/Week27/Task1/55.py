# Создайте декоратор, который перехватывает исключения, возникающие при выполнении функции, и выводит их на экран.
import time
from functools import wraps


def exception_handler_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception '{e}' occurred.")

    return wrapper


@exception_handler_decorator
def example_function(x, y):
    result = x / y
    print("Result:", result)


example_function(10, 6)
