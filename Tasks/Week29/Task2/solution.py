class Book:
    def __init__(self, title, author, number_pages, age):
        self.title = title
        self.author = author
        self.number_pages = number_pages
        self.age = age


class Fridge:
    def __init__(self, brand, capacity, model):
        self.brand = brand
        self.capacity = capacity
        self.model = model
        self.open_the_door = False
        self.turn_on_device = False

    def open_the_door(self):
        if not self.open_the_door:
            print("Дверца открыта")
            self.open_the_door = True
        else:
            print("Дверца уже открыта")

    def close_the_door(self):
        if self.open_the_door:
            print("Дверца закрыта")
            self.open_the_door = False
        else:
            print("Дверца уже закрыта")

    def turn_on_device(self):
        if not self.turn_on_device:
            print("Устройство включено")
            self.turn_on_device = True
        else:
            print("Устройство уже включено")
