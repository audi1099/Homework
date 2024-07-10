# Создайте класс "Человек". У него должны быть атрибуты, такие как имя, фамилия, возраст и номер телефона. Также
# создайте метод "встать" и "сесть".

class Human:
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.stand_up = False
        self.sit_down = False

    def stand_up(self):
        if not self.stand_up:
            print("Встать")
            self.stand_up = True
        else:
            print("Уже встал")

    def sit_down(self):
        if not self.sit_down:
            print("Сесть")
            self.sit_down = True
        else:
            print("Уже сижу")


person_1 = Human(name="Ivan", surname="Ivanov", age="45", phone="54354354")
print(person_1.name, person_1.surname, person_1.age, person_1.phone)
Human.stand_up(person_1)
Human.sit_down(person_1)
print("-----------------------------------------------")
