def find_numbers_divisible_by_3_and_5(start, end):
    numbers = [i for i in range(start, end) if i % 3 == 0 and i % 5 == 0]
    return numbers
