a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
list_1 = [(a % 2) == 0]
list_2 = [(b % 2) == 0]
even_numbers = [i for i in range(a, b+1) if i % 2 == 0]
print("Список четных чисел от 'a', до 'b': ", even_numbers)


