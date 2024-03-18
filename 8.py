def numbers_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = numbers_fibonacci()
for _ in range(8):
    print(next(fibonacci))

