def generate_even_numbers():
  i = 0
  while True:
    yield i
    i += 2

even_number_generator = generate_even_numbers()
for even_num in even_number_generator:
  print(even_num)
  if even_num > 10:
    break