def sort_by_age(lst):
    return sorted(lst, key=lambda x: x["age"], reverse=True)
