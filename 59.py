# 1. Создайте класс "Книга". У него должны быть атрибуты, такие как название книги, автор, количество страниц и год
# публикации.


class Book:
    def __init__(self, title, author, number_pages, age):
        self.title = title
        self.author = author
        self.number_pages = number_pages
        self.age = age


book_1 = Book(title="Maugli", author="Pupkin", number_pages="140", age="1985")
book_2 = Book(title="GHGJKHK", author="Nepupkin", number_pages="197", age="1965")
book_3 = Book(title="Earh", author="Ivanov", number_pages="65", age="1935")
print(book_1.title, book_1.author, book_1.number_pages, book_1.age)
print(book_2.title, book_2.author, book_2.number_pages, book_2.age)
print(book_3.title, book_3.author, book_3.number_pages, book_3.age)
print("------------------------------------------------------------------------------------")


# 2.Создайте класс "Автомобиль". У него должны быть атрибуты, такие как марка, модель, год выпуска и цвет. Также
#  создайте метод "завести двигатель".


class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.engine_started = False

    def start_engine(self):
        if not self.engine_started:
            print("Двигатель запущен.")
            self.engine_started = True
        else:
            print("Двигатель уже запущен.")


car_1 = Car(brand="BMW", model="750", year="2005", color="black")
print(car_1.brand, car_1.model, car_1.year, car_1.color)
car_1.start_engine()
print("------------------------------------------------------------------------------------")


# 3. Создайте класс "Холодильник". У него должны быть атрибуты, такие как производитель, емкость и название модели.
# Также создайте методы "открыть дверцу", "закрыть дверцу" и "включить устройство".


class Fridge:
    def __init__(self, brand, capacity, model):
        self.brand = brand
        self.capacity = capacity
        self.model = model
        self.Open_the_door = False
        self.Turn_on_device = False

    def open_the_door(self):
        if self.open_the_door:
            print("Дверца открыта")
            self.Open_the_door = True
        else:
            print("Дверца уже открыта")

    def close_the_door(self):
        if self.open_the_door:
            print("Дверца закрыта")
            self.Open_the_door = False
        else:
            print("Дверца уже закрыта")

    def turn_on_device(self):
        if not self.Turn_on_device:
            print("Устройство включено")
            self.Turn_on_device = True
        else:
            print("Устройство уже включено")


refrig = Fridge(brand="Horizont", capacity="350", model="1234")
print(refrig.brand, refrig.capacity, refrig.model)
refrig.open_the_door()
refrig.close_the_door()
refrig.turn_on_device()
print("------------------------------------------------------------------------------------")


# 4. Создайте класс "Человек". У него должны быть атрибуты, такие как имя, фамилия, возраст и номер телефона. Также
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
print("------------------------------------------------------------------------------------")


# 5. Создайте класс "Квадрат". У него должны быть атрибуты, такие как длина стороны и цвет.
# Также создайте метод "посчитать периметр" и "посчитать площадь".


class Square:
    def __init__(self, side_length, color):
        self.side_length = side_length
        self.color = color

    def calculate_perimeter(self):
        return 4 * self.side_length

    def calculate_area(self):
        return self.side_length ** 2


square_1 = Square(side_length=9, color="красный")
print(f"Квадрат со стороной {square_1.side_length} и цветом {square_1.color}")
perimeter = square_1.calculate_perimeter()
print("Периметр квадрата =", perimeter)
area = square_1.calculate_area()
print("Площадь квадрата =", area)
print("------------------------------------------------------------------------------------")


# 6. Создайте класс "Дом". У него должны быть атрибуты, такие как количество этажей, площадь и количество комнат.
# Также создайте метод "посчитать стоимость".

class House:
    def __init__(self, floors, maidan, rooms):
        self.floors = floors  # Количество этажей
        self.maidan = maidan  # Площадь
        self.rooms = rooms  # Количество комнат

    def calculate_cost(self):
        cost_per_square_meter = 1000  # Стоимость за квадратный метр
        cost_per_room = 18000  # Стоимость за комнату

        total_cost = self.maidan * cost_per_square_meter + self.rooms * cost_per_room
        return total_cost


house_1 = House(floors=2, maidan=150, rooms=7)
print(f"Мой дом: {house_1.floors} этаж, площадь {house_1.maidan} кв.м, {house_1.rooms} комнат")
cost = house_1.calculate_cost()
print("Стоимость дома:", cost)
print("------------------------------------------------------------------------------------")


# 7 Создайте класс "Телефон", у которого есть атрибут "Список контактов"
# в виде списка словарей
# :[ {"name": "Alex", "phone": "+375(29)123-45-67"}]и метод, принимающий номер телефона контакта или его
# имя и осуществляет вызов
class Telefon:
    def __init__(self, contact_list):
        self.contact_list = contact_list

    def call(self, name_or_fone):
        for contact in self.contact_list:
            if contact["name"] == name_or_fone or contact["phone"] == name_or_fone:
                print(f"Звоню: {contact['name']} - {contact['phone']}")
                break
            else:
                print("Контакт не найден")


contact_list = [{"name": "Alex", "phone": "+375(29)123-45-69"}]
phone_1 = Telefon(contact_list)
phone_1.call("Alex")
phone_1.call("Bob")
print("------------------------------------------------------------------------------------")