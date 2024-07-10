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