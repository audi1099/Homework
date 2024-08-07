# Написать функцию, которая принимает дерево, представленное в виде списка списков, где каждый элемент списка может
# быть либо числом, либо подсписком, и возвращает сумму всех чисел в дереве.
# пример: [1, 2, [3, 4, [5, 6]], [12, 13], 11, 10]
def sum_numbers(tree):
    result = 0
    for i in tree:
        if isinstance(i, list):
            result += sum_numbers(i)
        else:
            result += i
    return result


tree = [0, 4, [7, [3, 4], 5], 4]
print("Сумма чисел в дереве:", sum_numbers(tree))
