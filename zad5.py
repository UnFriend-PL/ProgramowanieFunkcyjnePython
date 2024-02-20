def get_even_numbers(n):
    evenList = []
    for i in n:
        if i % 2 == 0:
            evenList.append(i)
    return evenList


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


area_of_rectangle = lambda a, b: a * b

print(get_even_numbers(list))

print(area_of_rectangle(2, 3))
