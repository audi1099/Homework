def count_even_digits(number):
    count_even = 0
    sum_even = 0

    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            count_even += 1
            sum_even += digit
        number //= 10

    return count_even, sum_even
