def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


fibonacci_gen = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci_gen))

file_path = 'lorem.txt'
for line in read_large_file(file_path):
    print(line)