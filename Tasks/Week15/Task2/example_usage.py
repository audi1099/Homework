from solution import greet_user


def main():
    my_name = input("Введите ваше имя: ")
    year_of_birth = int(input("Введите год рождения: "))

    age = 2023 - year_of_birth

    print("Тип переменной my_name:", type(my_name))
    print("Тип переменной year_of_birth:", type(year_of_birth))
    print("Тип переменной age:", type(age))

    greet_user(my_name, age)


if __name__ == "__main__":
    main()
