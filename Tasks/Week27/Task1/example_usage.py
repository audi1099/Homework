from solution import exception_handler_decorator


@exception_handler_decorator
def example_function(x, y):
    result = x / y
    print("Result:", result)


def main():
    example_function(10, 0)  # Передаем некорректные аргументы для генерации исключения


if __name__ == "__main__":
    main()
