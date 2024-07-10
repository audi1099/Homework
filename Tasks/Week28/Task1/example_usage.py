from solution import coordinate


def main():
    try:
        start_x = 0
        start_y = 0
        directions = "SSWE"
        result_coordinate = coordinate(start_x, start_y, directions)
        print("Координата: ", result_coordinate)
    except ValueError as ve:
        print("Ошибка:", ve)
    except Exception as e:
        print("Произошла ошибка:", e)


if __name__ == "__main__":
    main()
