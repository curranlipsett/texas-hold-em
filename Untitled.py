class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        theRank = self.rank
        switch = {
            "Ace": 14,
            "King": 13,
            "Queen": 12,
            "Jack": 11,
            "Ten": 10,
            "Nine": 9,
            "Eight": 8,
            "Seven": 7,
            "Six": 6,
            "Five": 5,
            "Four": 4,
            "Three": 3,
            "Two": 2
        }

        return switch.get(self.rank, "Error")
