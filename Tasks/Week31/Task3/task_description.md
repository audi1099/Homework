# Описание задачи

## Задача

Создать классы "Human" и "House" для описания человека и дома соответственно. Реализовать методы для покупки дома, заработка денег и вывода информации о человеке. Также реализовать функцию для рекомендации дома на основе финансового положения и возраста человека.

### Класс `Human`

```python
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
        print(f"Наличие собственного жилья: {'Да' if self.has_own_home else 'Нет'}
