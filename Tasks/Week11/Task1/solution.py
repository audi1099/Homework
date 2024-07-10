from typing import List


def squares_of_even_divisible_by_5(n: int) -> List[int]:
    result = []
    for i in range(1, n+1):
        if i % 2 == 0 and i % 5 == 0:
            result.append(i**2)
    return result
