from solution import check_even_odd

number = int(input("Введите число: "))
result = check_even_odd(number)

if result:
    print("Число четное")
else:
    print("Число нечетное")
