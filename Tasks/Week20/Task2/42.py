# Создайте генератор, который будет возвращать только четные числа из заданного диапазона.
def square_numbers():
    for i in range(1, 32):
        if i % 2 == 0:
            yield i


for number in square_numbers():
    print(number)
