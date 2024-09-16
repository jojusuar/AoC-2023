archive = open('input.txt', 'r')
lines = archive.readlines()
archive.close()

maps = []
separator = 0
for i in range(len(lines)):
    line = (lines[i]).strip()
    if(len(line) == 0):
        maps.append(lines[separator:i])
        separator = i
maps.append(lines[separator:])

seeds = list(map(lambda x: int(x), maps[0][0].split(': ')[1].strip().split(' ')))
maps.pop(0)

for i in range(len(maps)):
    maps[i] = list(map(lambda line: line.strip().split(' '), maps[i][2:]))
    for j in range(len(maps[i])):
        maps[i][j] = list(map(lambda x: int(x), maps[i][j]))

def getLocation(seed):
    currentId = seed
    i = 0
    while(i < len(maps)):
        currentMap = maps[i]
        for entry in currentMap:
            sourceFloor = entry[1]
            sourceTop = sourceFloor + entry[2]
            if sourceFloor <= currentId < sourceTop:
                differential = currentId - sourceFloor
                currentId = entry[0] + differential
                break
        i += 1
    return currentId
    
part1 = list(map(getLocation, seeds))
part1.sort()
print(f'PART 1: {part1[0]}')

ranges = []
processed = []
i = 0
while(i < len(seeds) - 1):
    ranges.append([seeds[i], seeds[i + 1]])
    i += 2

for mappy in maps:
    while(len(processed) != 0):
        ranges.append(processed.pop(0))
    while(len(ranges) != 0):
        interval = ranges[0]
        differential = interval[1]
        sourceFloor = interval[0]
        sourceTop = sourceFloor + differential
        mapped = False
        for entry in mappy:
            targetFloor = entry[1]
            targetTop = entry[2] + targetFloor
            mappedFloor = entry[0]
            if(targetFloor <= sourceFloor and sourceTop <= targetTop):
                offset = mappedFloor - targetFloor
                ranges.pop(0)
                processed.append([sourceFloor + offset, differential])
                mapped = True
                break
            elif(sourceFloor < targetFloor < sourceTop):
                newInterval1 = [sourceFloor, targetFloor - sourceFloor]
                newInterval2 = [targetFloor, differential - newInterval1[1]]
                ranges.pop(0)
                ranges += [newInterval1, newInterval2]
                mapped = True
                break
            elif(sourceFloor < targetTop < sourceTop):
                newInterval1 = [targetTop, sourceTop - targetTop]
                newInterval2 = [sourceFloor, differential - newInterval1[1]]
                ranges.pop(0)
                ranges += [newInterval1, newInterval2]
                mapped = True
                break
        if(not mapped):
            processed.append(ranges.pop(0))

processed = sorted(processed, key = lambda interval: interval[0])
print(f'PART 2: {processed[0][0]}')    