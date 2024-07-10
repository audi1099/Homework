from solution import find_max_min

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

max_num, min_num = find_max_min(number_1, number_2)

print("Наибольшее число:", max_num)
print("Наименьшее число:", min_num)
