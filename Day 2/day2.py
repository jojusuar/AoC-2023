from functools import reduce

archive = open('input.txt', 'r')
lines = archive.readlines()
archive.close()

dicc = {'red': 12, 'green': 13, 'blue': 14}

#part 1
def checker(line):
    components = line.split(': ')
    header = components[0]
    idNumber = int(header.split(' ')[1])
    sets = components[1].split('; ')
    for zet in sets:
        cubeFrequencies = zet.split(', ')
        for frequency in cubeFrequencies:
            data = frequency.split(' ')
            number = int(data[0])
            color = data[1].strip()
            if(number > dicc[color]): return 0
    return idNumber

results = list(map(checker, lines))
total = reduce(lambda x, y: x + y, results)

print(total)

#part 2
def powerFinder(line):
    minimums = {'red': 0, 'green': 0, 'blue': 0}
    components = line.split(': ')
    sets = components[1].split('; ')
    for zet in sets:
        cubeFrequencies = zet.split(', ')
        for frequency in cubeFrequencies:
            data = frequency.split(' ')
            number = int(data[0])
            color = data[1].strip()
            if(number > minimums[color]): 
                minimums[color] = number
    return reduce(lambda x, y: x*y, minimums.values())

results2 = list(map(powerFinder, lines))
total = reduce(lambda x, y: x + y, results2)

print(total)