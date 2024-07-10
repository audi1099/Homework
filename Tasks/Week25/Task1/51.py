a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
squares_1 = [a ** 2]
squares_2 = [b ** 2]
squares_3 = [i ** 2 for i in range(a, b + 1)]
print("Список квадратов чисел от 'a', до 'b': ", squares_3)


