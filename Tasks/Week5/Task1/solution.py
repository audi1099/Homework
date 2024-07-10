def is_lucky_ticket(ticket_number):
    if len(ticket_number) != 6 or not ticket_number.isdigit():
        print("Некорректный ввод номера билета.")
        return False

    first_half_sum = sum(int(digit) for digit in ticket_number[:3])
    second_half_sum = sum(int(digit) for digit in ticket_number[3:])

    return first_half_sum == second_half_sum
