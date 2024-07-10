from solution import create_student_dict


def main():
    students = create_student_dict()

    # Выводим содержимое словаря
    for ticket_number, name in students.items():
        print(f"Студенческий билет №{ticket_number}: {name}")


if __name__ == "__main__":
    main()
