# Напишите программу, которая создает кортеж на 15 элементов, заполненный квадратами целых
# чисел от 1 до 15. В качестве результата работы выведите все элементы кортежа в порядке убывания.
a = tuple(i ** 2 for i in range(-15, 0))
print(a)