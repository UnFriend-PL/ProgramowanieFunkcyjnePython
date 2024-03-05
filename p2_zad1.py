import itertools


list1 = ['A', 'B']
list2 = ['C', 'D']

combinations = list(itertools.product(list1, list2))

for combination in combinations:
    print(combination)