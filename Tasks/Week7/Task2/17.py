# Написать функцию, принимающую число и возвращающую следующий за этим числом палиндром.
def palindrome(number):
    while True:
        number += 1
        if str(number) == str(number)[::-1]:
            return number


input_number = int(input())
result = palindrome(input_number)
print(f"{input_number}: {result}")
