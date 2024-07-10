from solution import Restaurant

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
