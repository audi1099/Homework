from solution import Book


def main():
    book_1 = Book(title="Maugli", author="Pupkin", number_pages=140, year_published=1985)
    book_2 = Book(title="GHGJKHK", author="Nepupkin", number_pages=197, year_published=1965)
    book_3 = Book(title="Earh", author="Ivanov", number_pages=65, year_published=1935)

    print("Book 1:", book_1.title, book_1.author, book_1.number_pages, book_1.year_published)
    print("Book 2:", book_2.title, book_2.author, book_2.number_pages, book_2.year_published)
    print("Book 3:", book_3.title, book_3.author, book_3.number_pages, book_3.year_published)


if __name__ == "__main__":
    main()
