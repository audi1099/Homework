def find_min_max(a, b):
    if a > b:
        return b, a
    elif a < b:
        return a, b
    else:
        return a, b  # или return a, a (если числа равны, можно вернуть любое из них)
