numbers = [5, 12, 7, 15, 3, 11, 20]
squares = [square for num in numbers if (square := num * num) > 10]
print(squares)