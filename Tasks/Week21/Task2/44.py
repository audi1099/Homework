# Реализуйте декоратор, который преобразует результат выполнения функции в верхний регистр
def upper_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@upper_decorator
def greet():
    return "redrdyy, dfdhgfh gjhgjhkjh vjghi"


print(greet())


