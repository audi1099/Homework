from solution import Telefon


def main():
    contact_list = [{"name": "Alex", "phone": "+375(29)123-45-69"}]
    phone_1 = Telefon(contact_list)

    phone_1.call("Alex")
    phone_1.call("+375(29)123-45-69")
    phone_1.call("Bob")

    print("------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
