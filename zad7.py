def num_to_square(num):
    return num ** 2
def add_five(num):
    return num + 5

print(num_to_square(5))
print(add_five(5))

def check_value_for_function(f, x):
    for i in x:
        for function in f:
            print(f'funkcja {function.__name__} - {function(i)}')

check_value_for_function([num_to_square, add_five], [1, 2, 3, 4, 5])