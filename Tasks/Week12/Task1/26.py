# Напишите программу, которая получает на вход целое
# положительное число с клавиатуры. Необходимо, используя цикл while, вывести количество
# четных цифр в этом числе и их сумму.
a = int(input('Введите любое целое число: '))
b = 0
c = 0
x = 0

while a > 0:
    if a % 2 == 0:
        b += 1
        x += a % 10
    else:
        c += 1
    a = a // 10

print(f'четные: {b}, нечетные: {c}')
print('Сумма четных цифр:', x)