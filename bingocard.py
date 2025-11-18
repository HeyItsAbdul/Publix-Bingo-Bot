import json
import random
import textwrap

with open('storage.json', 'r') as file:
    storage = json.load(file)
events = storage['events'] 

class BingoCard:
    def __init__(self, owner):
        self.owner = owner
        self.bingoCard = [[-1 for i in range(5)] for j in range(5)]
        self.GenerateBingoCard()
        
    def GenerateBingoCard(self):
        randNums = random.sample(range(len(events)),25)
        randNums[13] = -1
        curr = 0
        self.bingoCard[0][0] = 24

        for i in range(5):
          for j in range(5):
            self.bingoCard[i][j] = randNums[curr]
            curr += 1
