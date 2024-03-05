import itertools

def get_combinations(input_list):
    return list(itertools.combinations(input_list, 2))

list1 = ['A', 'B', 'C', 'D']
combinations = get_combinations(list1)
print(combinations)
