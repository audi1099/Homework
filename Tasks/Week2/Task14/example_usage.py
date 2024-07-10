from solution import check_divisibility

num_1 = int(input("Введите большее число: "))
num_2 = int(input("Введите меньшее число: "))

result, remainder = check_divisibility(num_1, num_2)

if result:
    print(f"{num_1} кратно {num_2}")
else:
    print(f"{num_1} не кратно {num_2}")
    print(f"Остаток от деления: {remainder}")
