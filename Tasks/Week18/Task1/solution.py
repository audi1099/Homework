def special_number(number):
    allowed_digits = set("012345")
    for digit in str(number):
        if digit not in allowed_digits:
            return False
    return True
