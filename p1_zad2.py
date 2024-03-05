def make_multiplier(multiplier):
    def multiply(x):
        return x * multiplier
    return multiply
multiplier2 = make_multiplier(2)
multiplier3 = make_multiplier(3)

print(multiplier2(5))
print(multiplier3(5))