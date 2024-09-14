def lineProcessor(string):
    halves = string[9:].strip().replace('  ',' ').split(' | ')
    winningNumbers = set(halves[0].split(' '))
    myNumbers = set(halves[1].split(' '))
    return (winningNumbers, myNumbers)

def cardCalculator(set1, set2):
    intersection = set1 & set2
    matches = len(intersection)
    return matches

lines = open('input.txt').readlines()
part1 = 0
cards = [1] * len(lines)
for i, line in enumerate(lines):
    processed = lineProcessor(line)
    matches = cardCalculator(processed[0], processed[1])
    if matches > 0:
        part1 += 2**(matches-1)
    for j in range(i+1, min(i+1+matches, len(lines))):
        cards[j] += cards[i]
part2 = sum(cards)

print(part1, part2)
