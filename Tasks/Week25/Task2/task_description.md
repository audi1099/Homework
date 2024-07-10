# Описание задачи

## Задача

Напишите программу, которая запрашивает у пользователя строку, находит все гласные буквы в этой строке и выводит список строк, содержащих только гласные буквы.

## Функция в solution.py

### Функция extract_vowel_strings

```python
def extract_vowel_strings(input_string):
    vowels = "AEIOUaeiou"
    vowel_strings = [i for i in input_string if i in vowels]
    return vowel_strings
