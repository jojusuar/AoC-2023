archive = open('input.txt', 'r')
lines = list(archive.readlines())
archive.close()

part1 = 0

def isAdjacent(number):
    for x in number['columns']:
        for y in number['rows']:
            symbol = lines[y][x]
            if(not (symbol.isdigit() or symbol == '.' or symbol == '\n')):
                return True
    return False
                
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
                number['left'] = False
            if number['columns'][-1] < len(row) - 1:
                number['columns'].append(number['columns'][-1] + 1)
                number['right'] = False
            if 0 < number['rows'][0]:
                number['rows'].insert(0, number['rows'][0] - 1)
                number['top'] = False
            if number['rows'][-1] < len(lines) -1:
                number['rows'].append(number['rows'][-1] + 1)
                number['bottom'] = False
            
            if(isAdjacent(number)):
                part1 += int(number['number'])
        j += 1
        
print(part1)