# еализуйте декоратор, который добавляет задержку перед выполнением функции


import time
from functools import wraps


def delay_decorator(delay_time):
    def exception_handler_decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(delay_time)
            return func(*args, **kwargs)
        return wrapper
    return exception_handler_decorator


@delay_decorator(4)
def example_function(x, y):
    result = x / y
    print("Result:", result)


example_function(10, 2)
