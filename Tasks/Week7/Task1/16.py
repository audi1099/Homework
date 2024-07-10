# Написать функцию, которая принимает список словарей, где каждый словарь представляет
# собой запись об ученике (с ключами 'имя', 'возраст', 'оценки'), и возвращает список словарей, отсортированный по
# возрасту учеников в порядке убывания.
def sort_by_age(lst):
    return sorted(lst, key=lambda x: x["age"], reverse=True)


a = [dict(name="John", age="25", ratings=[5, 3, 5, 4, 4, 3, 5]),
     dict(name="Vitaliy", age="41", ratings=[5, 4, 5, 4, 4, 4, 5]),
     dict(name="Vlad", age="19", ratings=[5, 4, 5, 4, 4, 5, 5]),
     dict(name="Oleg", age="29", ratings=[5, 5, 5, 3, 4, 3, 5])]

print(sort_by_age(a))



