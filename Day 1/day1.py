from functools import reduce

archive = open('input.txt', 'r')
lines = list(archive.readlines())

total = 0

dicc = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

for line in lines:
    characters = list(line)
    # numList = list(filter(lambda character: character.isdigit(), characters))
    # numString = numList[0] + numList[-1]
    # number = int(numString)
    # total += number
    
    #part 2
    tuples = []
    for key in dicc.keys():
        start = 0
        index = line.find(key, start)
        while(index != -1):
            tuples.append((index, dicc[key]))
            start += len(key)
            index = line.find(key, start)
    for i in range(len(characters)):
        character = characters[i]
        if(character.isdigit()):
            tuples.append((i, character))
    sorted_tuples = sorted(tuples, key = lambda tuple: tuple[0])
    numString = str(sorted_tuples[0][1]) + str(sorted_tuples[-1][1])
    number = int(numString)
    total += number
    
print(total) 