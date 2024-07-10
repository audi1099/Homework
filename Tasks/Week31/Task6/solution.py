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
