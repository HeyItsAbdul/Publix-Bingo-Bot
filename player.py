class Player:
    def __init__(self, playerName, bingoCard):
        self.name = playerName
        self.card = bingoCard

    def print(self):
        print('Name: ' + self.name)
        print('BingoCard Codes: ')
        self.card.print()
    