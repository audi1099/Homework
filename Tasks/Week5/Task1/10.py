# Написать программу, определяющую является ли введенный номер билета - "счастливым".
# Билет называют «счастливым», если в его номере сумма первых трех цифр равна сумме последних трех.
# Номер билета может быть от 000000 до 999999.
ticket_number = input("Введите номер билета (от 000000 до 999999): ")
if len(ticket_number) != 6 or not ticket_number.isdigit():
    print("Некоректный ввод номера билета: ")
else:

    first_half_sum = sum(int(digit) for digit in ticket_number[:3])
    second_half_sum = sum(int(digit) for digit in ticket_number[3:])
    if first_half_sum == second_half_sum:

        print("Этот билет - счастливый!")
    else:
        print("Этот билет не счастливый.")
