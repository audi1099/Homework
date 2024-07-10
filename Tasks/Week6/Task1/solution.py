def sum_numbers(tree):
    result = 0
    for item in tree:
        if isinstance(item, list):
            result += sum_numbers(item)
        else:
            result += item
    return result
