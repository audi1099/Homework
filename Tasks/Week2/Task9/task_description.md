# Task Description

## Objective

Write a function `filter_divisible_by_3(numbers)` that takes a list of numbers as input and returns a new list containing only the numbers that are divisible by 3 without a remainder, using a lambda function.

## Example Usage

```python
from solution import filter_divisible_by_3

a = [9, 4, 5, 16, 27, 8, 19, 30, 3]
new_list = filter_divisible_by_3(a)
print(new_list)  # Output: [9, 27, 30, 3]
