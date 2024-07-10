def check_divisibility(num1, num2):
    if num1 % num2 == 0:
        print(f"{num1} кратно {num2}")
    else:
        remainder = num1 % num2
        print(f"{num1} не кратно {num2}, остаток от деления: {remainder}")
