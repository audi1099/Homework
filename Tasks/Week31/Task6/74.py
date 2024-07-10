class Car:
    instances = 0

    def __init__(self, mileage, name, year, price):
        self.mileage = mileage
        self.name = name
        self.year = year
        self.price = price
        Car.instances += 1

    def __str__(self):
        return f"Car: {self.name}, Year: {self.year}"

    def __eq__(self, other):
        return self.name == other.name and self.year == other.year

    def price_in_dollars(self, exchange_rate=0.30):  # 1 rubles = 0.30 dollar
        return self.price * exchange_rate

    @classmethod
    def get_instance_count(cls):
        return cls.instances

    @staticmethod
    def get_country_of_origin(brand):
        if brand.lower() == "toyota":
            return "Japan"
        elif brand.lower() == "bmw":
            return "Germany"
        elif brand.lower() == "ford":
            return "USA"
        else:
            return "Unknown"

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value >= 0:
            self._mileage = value
        else:
            raise ValueError("Пробег не может быть отрицательным")

    @mileage.deleter
    def mileage(self):
        del self._mileage

    @property
    def mileage_info(self):
        return f"Автомобиль имеет пробег {self.mileage} миль."


class ToyotaCar(Car):
    @staticmethod
    def get_country_of_origin(brand):
        return "Japan"


car1 = Car(10000, "Toyota Camry", 2022, 52000)
car2 = Car(20000, "Toyota Camry", 2022, 31000)
car3 = Car(15000, "BMW X5", 2020, 42000)

print(car1 == car2)  # True, так как у них одинаковое название и год
print(car1.price_in_dollars())
print(Car.get_instance_count())
print(Car.get_country_of_origin("Toyota"))
print(Car.get_country_of_origin("Ford"))

toyota_car = ToyotaCar(30000, "Toyota Corolla", 2021, 27000)
print(ToyotaCar.get_country_of_origin("Toyota"))

print(car1.mileage_info)

car1.mileage = 12000
print(car1.mileage_info)

del car1.mileage


