# 1. Напишите функцию, которая принимает список чисел и возвращает новый список, содержащий
# только четные числа, используя lambda функцию.
# a = [3, 4, 5, 16, 27, 8, 19,]
# new_list = list(filter(lambda n: n % 2 == 0, a))
# print(new_list)


# 2. Напишите функцию, которая принимает два числа и возвращает их сумму, используя lambda функцию.
# print((lambda a, b: a + b)(1, 800))


# 3. Напишите функцию, которая принимает список строк и возвращает новый список, содержащий
# только строки длиной больше 3 символов, используя lambda функцию.
# def filter_strings(strings):
#    return list(filter(lambda x: len(x) > 3, strings))
# strings = ["sds", "er", "weetr"]
# filtered_strings = filter_strings(strings)
# print(filtered_strings)


# 4. Напишите функцию, которая принимает список чисел и возвращает новый
# список, содержащий квадраты этих чисел, используя lambda функцию.
# a = [2, 4, 5, 16, 27, 8, 19,]
# new_list = list(map(lambda n: n ** 2, a))
# print(new_list)


# 5.Напишите функцию, которая принимает список слов и возвращает новый список, содержащий
# только слова, начинающиеся с буквы "а" или “A”, используя lambda функцию.
# def filter_words(word_list):
#    return list(filter(lambda word: word[0].lower() == 'a', word_list))


# words = ["alenjbj", "bftfugu", "Ant", "dog", "Adfddg"]
# filtered_words = filter_words(words)
# print(filtered_words)


# 6. Напишите функцию, которая принимает список чисел и возвращает новый
# список, содержащий только числа больше 10, используя lambda функцию.
# a = [2, 4, 5, 16, 27, 8, 19, 11, 13, 19]
# new_list = list(filter(lambda n: n > 10, a))
# print(new_list)


# 7. Напишите функцию, которая принимает список строк и возвращает новый список, содержащий
# только строки в верхнем регистре, используя lambda функцию.
# def to_uppercase(strings):
#    return list(filter(lambda x: x.isupper(), strings))


# strings = ["ETRE", "ddfd", "Rfhh", "Tuuy", "TYTYUT"]
# print(to_uppercase(strings))


# 8. Напишите функцию, которая принимает список чисел и возвращает новый список, содержащий
# только числа, делящиеся на 3 без остатка, используя lambda функцию
# a = [9, 4, 5, 16, 27, 8, 19, 30, 3]
# new_list = list(filter(lambda n: n % 3 == 0, a))
# print(new_list)


# 9. Напишите функцию, которая принимает список чисел и возвращает новый список, содержащий
# только числа в диапазоне от 5 до 10, используя lambda функцию.
# def filter_numbers(number):
#    return list(filter(lambda x: 5 <= x <= 10, number))


# numbers = [1, 12, 8, 4, 9, 11, 7]
# print(filter_numbers(numbers))


# 10. Напишите функцию, которая принимает список строк и возвращает новый список, содержащий только
# строки, оканчивающиеся на букву "о", используя lambda функцию.
# def filter_words(word_list):
#     return list(filter(lambda word: word.endswith('o'), word_list))


# words = ["alenjbo", "bftfugo", "Ant", "dogpo", "Adfddg"]
# filtered_words = filter_words(words)
# print(filtered_words)
