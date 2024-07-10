# Создайте класс "Дом". У него должны быть атрибуты, такие как количество этажей, площадь и количество комнат.
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
