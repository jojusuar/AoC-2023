import heapq
import time
starttime = time.time()
order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

class Hand:
    def __init__(self, string, bet):
        self.cards = string[:]
        self.bet = bet
        dic = {}
        for card in self.cards:
            value = dic.get(card, 0)
            dic[card] = value + 1
        coincidences = []
        for key in dic:
            coincidences.append(dic[key])
        coincidences.sort(reverse=True)
        strength = 0
        mode = coincidences[0]
        if mode == 5:
            strength = 6
        elif mode == 4:
            strength = 5
        elif mode == 3:
            strength = 3
            if coincidences[1] == 2:
                strength += 1
        elif mode == 2:
            strength = 1
            if coincidences[1] == 2:
                strength += 1
            
        self.strength = strength
    
    def __lt__(self, other):
        if self.strength < other.strength:
            return True
        elif self.strength == other.strength:
            indexes = {card: index for index, card in enumerate(order)}
            pairs = list(zip(self.cards, other.cards))
            for pair in pairs:
                firsthand = indexes[pair[0]]
                secondhand = indexes[pair[1]]
                if firsthand > secondhand:
                    return True
                if firsthand < secondhand:
                    return False
        return False

heap = []

with open('D:/ESPOL/AoC-2023-Solutions/JoseJulioSuarez/Day 7/input.txt', 'r') as input:
    for line in input:
        data = line.split(' ')
        heapq.heappush(heap, Hand(data[0], data[1]))

counter = 0
total = 0
while heap:
    counter += 1
    total += int(heapq.heappop(heap).bet) * counter
print(total)
endtime = time.time()
print('Excecution time: ', (endtime - starttime)*1000 , 'milliseconds')

