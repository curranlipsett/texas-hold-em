from Card import *

myDeck = Deck()

print(myDeck.numCards)

for i in range(myDeck.numCards):
	print myDeck.getCard(i).getRank()
