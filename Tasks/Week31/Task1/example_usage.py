from solution import House


def main():
    house_1 = House(floors=2, area=150, rooms=7)
    print(f"Мой дом: {house_1.floors} этаж, площадь {house_1.area} кв.м, {house_1.rooms} комнат")

    cost = house_1.calculate_cost()
    print("Стоимость дома:", cost)

    print("------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
