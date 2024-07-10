def check_divisibility(num_1, num_2):
    if num_1 % num_2 == 0:
        print(f"{num_1} кратно {num_2}")
    elif num_1 == num_2:
        print("Они равны друг другу")
    else:
        remainder = num_1 % num_2
        print(f"{num_1} не кратно {num_2}")
        print(f"Остаток от деления: {remainder}")
