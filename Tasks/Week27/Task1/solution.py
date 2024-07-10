import time
from functools import wraps


def exception_handler_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception '{e}' occurred.")

    return wrapper
