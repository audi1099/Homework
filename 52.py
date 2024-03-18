array = str(input("Введите строку: "))
vowels = "AEIOUaeiou"
vowels_array = [i for i in array if i.lower() in "AEIOUaeiou"]
print("список строк содержащих только гласные буквы: ", vowels_array)

