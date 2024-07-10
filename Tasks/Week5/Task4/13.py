# Написать функцию, которая определит, является ли переданное число простым
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


test_number = 17
if is_prime(test_number):
    print(f"{test_number} - простое число")
else:
    print(f"{test_number} - не простое число")








