global_value = 10
def set_global_value(value):
    global_value = value
    print(f'global value: {global_value}')

set_global_value(5)