from solution import Book, Fridge


def main():
    book_1 = Book(title="Maugli", author="Pupkin", number_pages="140", age="1985")
    book_2 = Book(title="GHGJKHK", author="Nepupkin", number_pages="197", age="1965")
    book_3 = Book(title="Earh", author="Ivanov", number_pages="65", age="1935")

    print("Book 1:", book_1.title, book_1.author, book_1.number_pages, book_1.age)
    print("Book 2:", book_2.title, book_2.author, book_2.number_pages, book_2.age)
    print("Book 3:", book_3.title, book_3.author, book_3.number_pages, book_3.age)

    print("------------------------------------------------------------------------------------")

    refrig = Fridge(brand="Horizont", capacity="350", model="1234")
    print(refrig.brand, refrig.capacity, refrig.model)
    refrig.open_the_door()
    refrig.close_the_door()
    refrig.turn_on_device()

    print("------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
