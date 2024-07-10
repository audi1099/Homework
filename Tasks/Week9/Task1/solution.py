def sum_even_numbers(N):
    num = []
    for i in range(N + 1):
        if i % 2 == 0:
            num.append(i)
    return sum(num)
