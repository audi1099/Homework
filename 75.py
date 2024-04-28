class Restaurant:
    def __init__(self):
        self.menu = {}

    def add_dish(self, dish_name, price):
        if dish_name not in self.menu:
            self.menu[dish_name] = price
            print(f"Блюдо '{dish_name}' успешно добавлено в меню.")
        else:
            print(f"Блюдо '{dish_name}' уже есть в меню.")

    def remove_dish(self, dish_name):
        if dish_name in self.menu:
            del self.menu[dish_name]
            print(f"Блюдо '{dish_name}' успешно удалено из меню.")
        else:
            print(f"Блюдо '{dish_name}' не найдено в меню.")

    def order(self, *dishes):
        print("Заказанные блюда:")
        total_price = 0
        for dish in dishes:
            if dish in self.menu:
                print(f"- {dish}: {self.menu[dish]}")
                total_price += self.menu[dish]
            else:
                print(f"- {dish}: Блюдо не найдено в меню")
        print(f"Итого к оплате: {total_price}")


# Пример использования класса Restaurant
restaurant = Restaurant()

# Добавление блюд в меню
restaurant.add_dish("Пицца", 300)
restaurant.add_dish("Суп", 150)
restaurant.add_dish("Салат", 200)

# Удаление блюда из меню
restaurant.remove_dish("Суп")

# Заказ блюд
restaurant.order("Пицца", "Суп", "Бургер")
