class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model

    def __ne__(self, other):
        return not self.__eq__(other)


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def __str__(self):
        return super().__str__() + f", Doors: {self.doors}"


class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def __str__(self):
        return super().__str__() + f", Capacity: {self.capacity}"


class ElectricMixin:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f"Battery Capacity: {self.battery_capacity}"

    def __eq__(self, other):
        return self.battery_capacity == other.battery_capacity

    def __ne__(self, other):
        return not self.__eq__(other)


class ElectricCar(ElectricMixin, Car):
    def __init__(self, brand, model, doors, battery_capacity):
        Car.__init__(self, brand, model, doors)
        ElectricMixin.__init__(self, battery_capacity)

    def __str__(self):
        return Car.__str__(self) + ", " + ElectricMixin.__str__(self)
