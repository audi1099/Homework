def even_number_generator(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            yield i
