class Human:
    def __init__(self, name, age, money, has_own_home):
        """
        Инициализация объекта класса Human.

        Args:
            name (str): Имя человека.
            age (int): Возраст человека.
            money (float): Деньги, которые у человека есть.
            has_own_home (bool): Флаг, указывающий на наличие у человека собственного жилья.
        """
        self.name = name
        self.age = age
        self.money = money
        self.has_own_home = has_own_home

    def provide_info(self):
        """
        Выводит информацию о человеке.
        """
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Деньги: {self.money}")
        print(f"Наличие собственного жилья: {'Да' if self.has_own_home else 'Нет'}")

    def earn_money(self, amount):
        """
        Увеличивает количество денег человека.

        Args:
            amount (float): Сумма денег, которую человек заработал.
        """
        self.money += amount

    def buy_home(self, home):
        """
        Покупает дом, если у человека достаточно денег.

        Args:
            home (House): Объект класса House, который человек хочет купить.
        """
        if self.money >= home.discounted_price():
            self.money -= home.discounted_price()
            self.has_own_home = True
            print(f"{self.name} купил дом!")
        else:
            print("У вас недостаточно денег для покупки дома.")


class House:
    def __init__(self, area, price):
        """
        Инициализация объекта класса House.

        Args:
            area (int): Площадь дома в квадратных метрах.
            price (float): Стоимость дома.
        """
        self.area = area
        self.price = price

    def apply_discount(self, discount_percent):
        """
        Применяет скидку к стоимости дома.

        Args:
            discount_percent (float): Размер скидки в процентах.
        """
        self.price *= (1 - discount_percent / 100)

    def discounted_price(self):
        """
        Возвращает стоимость дома с учетом примененной скидки.

        Returns:
            float: Стоимость дома с учетом скидки.
        """
        return self.price

    def __str__(self):
        """
        Возвращает строковое представление объекта класса House.

        Returns:
            str: Строковое представление объекта класса House.
        """
        return f"Дом: площадь - {self.area} кв.м, стоимость - {self.price} долларов"


def recommend_house(human, houses):
    """
    Рекомендует дом для человека на основе его финансового положения и возраста.

    Args:
        human (Human): Человек, для которого делается рекомендация.
        houses (list): Список доступных домов.

    """
    affordable_houses = [house for house in houses if human.money >= house.discounted_price() and human.age >= 18]
    if affordable_houses:
        best_house = max(affordable_houses, key=lambda x: x.area)
        print(f"Рекомендация домов для {human.name}:")
        print(f"Лучший дом:")
        print(best_house)
    else:
        print("К сожалению, у вас недостаточно денег или вы не достигли совершеннолетия.")


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
