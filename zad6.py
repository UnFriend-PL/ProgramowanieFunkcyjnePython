wordList = ['cat', 'dog', 'rabbit', 'bird', 'elephant', 'dolphin' , 'ant', 'bat', 'bear', 'camel', 'deer', 'eagle', 'fish', 'goat', 'horse', 'iguana', 'jaguar', 'kangaroo', 'lion', 'monkey', 'newt', 'owl', 'panda', 'quail', 'rat', 'snake', 'tiger', 'unicorn', 'vulture', 'whale', 'xerus', 'yak', 'zebra']

print(list(filter(lambda x: x[0] == 'a', wordList)))

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x ** 2, numList)))
