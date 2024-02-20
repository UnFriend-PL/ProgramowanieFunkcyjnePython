def check_value_for_function(f, x):
    print(f(x))
    return f(x)
def is_even(x):
    return x % 2 == 0
def is_odd(x):
    return x % 2 != 0
check_value_for_function(is_even, 5)
check_value_for_function(is_odd, 5)
