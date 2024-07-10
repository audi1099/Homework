# Описание задачи

## Задача

Создать класс "Дом" с атрибутами: количество этажей, площадь и количество комнат. Добавить метод для расчета стоимости дома.

### Класс `House`

```python
class House:
    def __init__(self, floors, area, rooms):
        self.floors = floors  # Количество этажей
        self.area = area  # Площадь
        self.rooms = rooms  # Количество комнат

    def calculate_cost(self):
        cost_per_square_meter = 1000  # Стоимость за квадратный метр
        cost_per_room = 18000  # Стоимость за комнату

        total_cost = self.area * cost_per_square_meter + self.rooms * cost_per_room
        return total_cost
