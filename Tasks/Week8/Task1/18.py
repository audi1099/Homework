# Напишите генератор, который будет возвращать квадраты чисел от 1 до 10.
def square_numbers():
    for i in range(1, 11):
        yield i ** 2


for number in square_numbers():
    print(number)





