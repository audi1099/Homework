from solution import is_lucky_ticket

ticket_number = input("Введите номер билета (от 000000 до 999999): ")
is_lucky = is_lucky_ticket(ticket_number)

if is_lucky:
    print("Этот билет - счастливый!")
else:
    print("Этот билет не счастливый.")
