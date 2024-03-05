def filter_even_numbers(numbers):
  return list(filter(lambda x: x % 2 == 0, numbers))

numbers = [1, 2, 3, 4, 5]

even_numbers = filter_even_numbers(numbers)

print(even_numbers)