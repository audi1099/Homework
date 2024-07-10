from solution import Human, House, recommend_house

# Создание экземпляров классов
human1 = Human("Антон", 30, 300000, False)
human2 = Human("Кристина", 25, 240000, True)

house1 = House(100, 140000)
house2 = House(120, 160000)
house3 = House(80, 100000)

# Применение скидок на дома
house1.apply_discount(10)
house2.apply_discount(5)

# Проверка методов
human1.provide_info()
human1.buy_home(house1)
human1.provide_info()

human2.provide_info()
human2.buy_home(house3)
human2.provide_info()

# Рекомендация домов для людей
houses = [house1, house2, house3]
recommend_house(human1, houses)
recommend_house(human2, houses)
