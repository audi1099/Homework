# Определите является ли число специальным, по определение специальное число - это число, которое состоит
# только из чисел 0, 1, 2, 3, 4 или 5.
def special_number(number):
    allowed_digits = set("012345")
    for digit in str(number):
        if digit not in allowed_digits:
            return False

    return True


print(special_number(5))

































