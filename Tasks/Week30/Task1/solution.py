class Human:
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.stand_up_status = False
        self.sit_down_status = False

    def stand_up(self):
        if not self.stand_up_status:
            print("Встать")
            self.stand_up_status = True
        else:
            print("Уже встал")

    def sit_down(self):
        if not self.sit_down_status:
            print("Сесть")
            self.sit_down_status = True
        else:
            print("Уже сижу")
