
from Card import *

class Deck:
  
	def __init__(self,):
   # Initialize deck class to keep track of all cards, the cards being used (inPlay), and the number of cards in the deck to start
		self.cards = []
		self.inPlay = []
		self.numCards = 52

		for suit in range(4):
			for rank in range(13):
				self.cards.append(Card(rank, suit))


	def __str__(self):
		returnList = []
		for card in self.cards:
			returnList.append(str(card))

		return '\n'.join(returnList)
