def palindrome(number):
    while True:
        number += 1
        if str(number) == str(number)[::-1]:
            return number
