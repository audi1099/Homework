# Напишите программу, которая определяет наибольшее и наименьшее из двух чисел, введенных пользователем
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print("Число", a, "больше числа", b)
elif a == b:
    print("Эти числа равны")
else:
    print("Число", b, "больше числа", a)
