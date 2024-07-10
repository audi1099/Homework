def check_divisibility(num_1, num_2):
    if num_1 % num_2 == 0:
        return True, None
    else:
        remainder = num_1 % num_2
        return False, remainder
