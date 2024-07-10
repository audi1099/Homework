from solution import Car, ToyotaCar

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
