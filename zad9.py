import functools as ft
list = [99, 1, 3, 2, 5, 1, 0, 2, 101, 3, 4, 5, 6, 7, 8, 9]

def the_higher(x):
   return ft.reduce(lambda a, b: a if a > b else b, x)

def average(x):
    sum = ft.reduce(lambda a, b: a + b, x)
    avg = sum / len(x)
    return avg
print(average(list))
print(the_higher(list))