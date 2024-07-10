def upper_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper
