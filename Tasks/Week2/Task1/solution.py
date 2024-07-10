import sys

def get_user_info():
    my_name = input("Введите Ваше имя: ")

    year_of_birth = int(input("Введите год рождения: "))
    if year_of_birth > 2014:
        sys.exit("Вы ввели некорректные данные")

    age = 2024 - year_of_birth
    print("Здравствуйте", my_name, "Вам", age, "год")

if __name__ == "__main__":
    get_user_info()
