def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)

square = lambda x: x ** 2
print(square(5))

names = ["Anna", "Bob", "Charlie"]
ages = [25, 30, 22]
combined = list(zip(names, ages))
print(combined)

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

characters = ['a', 'A', 'z', 'Z', '1', '9', '@', '$']

min_char = min(characters, key=lambda x: ord(x))
max_char = max(characters, key=lambda x: ord(x))

print("Najmniejszy znak ASCII:", min_char)
print("Największy znak ASCII:", max_char)
