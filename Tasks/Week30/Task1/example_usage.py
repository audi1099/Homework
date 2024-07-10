from solution import Human


def main():
    person_1 = Human(name="Ivan", surname="Ivanov", age="45", phone="54354354")
    print(person_1.name, person_1.surname, person_1.age, person_1.phone)

    person_1.stand_up()
    person_1.sit_down()

    print("------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
