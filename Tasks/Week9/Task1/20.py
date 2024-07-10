# Напишите программу, вычисляющую сумму всех четных чисел от 0 до N (включительно).
# N - целое число, введенное пользователем.
# Для решения используйте цикл for.
a = int(input())
rt = list(range(a + 1))
print(rt)
num = []
for i in rt:
    if i % 2 == 0:
        num.append(i)
print(num[1::])
print(sum(num[1::]))

















