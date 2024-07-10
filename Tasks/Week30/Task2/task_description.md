# Описание задачи

## Задача

Создать класс "Квадрат" с атрибутами: длина стороны и цвет. Добавить методы для расчета периметра и площади квадрата.

### Класс `Square`

```python
class Square:
    def __init__(self, side_length, color):
        self.side_length = side_length
        self.color = color

    def calculate_perimeter(self):
        return 4 * self.side_length

    def calculate_area(self):
        return self.side_length ** 2
