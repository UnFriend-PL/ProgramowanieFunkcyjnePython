import functools

def safe_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Caught an error: {e}")
            return None
    return wrapper

@safe_function
def divide(a, b):
    return a / b

print(divide(10, 2))  # Outputs: 5.0
print(divide(10, 0))  # Outputs: Caught an error: division by zero
                    