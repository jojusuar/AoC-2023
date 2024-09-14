from functools import reduce

archive = open('input.txt', 'r')
lines = list(archive.readlines())
archive.close()

part1 = 0
part2 = 0
adjacencyTable = {} 

def isAdjacent(number):
    for x in number['columns']:
        for y in number['rows']:
            symbol = lines[y][x]
            if(not (symbol.isdigit() or symbol == '.' or symbol == '\n')):
                return True
    return False

def adjacencies(number):
    for x in number['columns']:
        for y in number['rows']:
            symbol = lines[y][x]
            if(not (symbol.isdigit() or symbol == '.' or symbol == '\n')):
                if(symbol == '*'):
                    numbers = adjacencyTable.get((x, y))
                    if(numbers is None):
                        adjacencyTable[(x, y)] = [int(number['number'])]
                    else:
                        adjacencyTable[(x, y)].append(int(number['number']))
                
for i in range(len(lines)):
    row = lines[i]
    j = 0
    while j < len(row):
        character = row[j]
        if(character.isdigit()):
            number = {'rows': [i], 'columns': [j], 'number': character}
            currentIdx = j + 1
            currentChar = row[currentIdx]
            while(currentChar.isdigit()):
                number['columns'].append(currentIdx)
                number['number'] += currentChar
                currentIdx += 1
                if(currentIdx < len(row)):
                    currentChar = row[currentIdx]
                else: break
            j = currentIdx
            
            if 0 < number['columns'][0]:
                number['columns'].insert(0, number['columns'][0] - 1)
            if number['columns'][-1] < len(row) - 1:
                number['columns'].append(number['columns'][-1] + 1)
            if 0 < number['rows'][0]:
                number['rows'].insert(0, number['rows'][0] - 1)
            if number['rows'][-1] < len(lines) -1:
                number['rows'].append(number['rows'][-1] + 1)
            
            if(isAdjacent(number)):
                part1 += int(number['number'])
            adjacencies(number)
        j += 1
        
print(part1)

for numberList in adjacencyTable.values():
    if(len(numberList) == 2):
        part2 += reduce(lambda x, y: x*y, numberList)

print(part2)