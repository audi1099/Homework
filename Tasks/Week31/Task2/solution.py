class Telefon:
    def __init__(self, contact_list):
        self.contact_list = contact_list

    def call(self, name_or_phone):
        found = False
        for contact in self.contact_list:
            if contact["name"] == name_or_phone or contact["phone"] == name_or_phone:
                print(f"Звоню: {contact['name']} - {contact['phone']}")
                found = True
                break

        if not found:
            print("Контакт не найден")
