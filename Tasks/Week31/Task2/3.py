# Создайте класс "Телефон", у которого есть атрибут "Список контактов"
# в виде списка словарей
# :[ {"name": "Alex", "phone": "+375(29)123-45-67"}]и метод, принимающий номер телефона контакта или его
# имя и осуществляет вызов
class Telefon:
    def __init__(self, contact_list):
        self.contact_list = contact_list

    def call(self, name_or_fone):
        for contact in self.contact_list:
            if contact["name"] == name_or_fone or contact["phone"] == name_or_fone:
                print(f"Звоню: {contact['name']} - {contact['phone']}")
                break
            else:
                print("Контакт не найден")


contact_list = [{"name": "Alex", "phone": "+375(29)123-45-69"}]
phone_1 = Telefon(contact_list)
phone_1.call("Alex")
phone_1.call("Bob")
print("------------------------------------------------------------------------------------")