import time
from functools import wraps

def delay_decorator(delay_time):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(delay_time)
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
