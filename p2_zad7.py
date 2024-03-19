from itertools import groupby

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.sort(key=lambda x: x % 2 == 0)
grouped_numbers = groupby(numbers, key=lambda x: x % 2 == 0)

for key, group in grouped_numbers:
    print(f"Parzyste: {key}, Liczby: {list(group)}")