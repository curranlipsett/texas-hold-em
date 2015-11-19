class Card:

	suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
	rank_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] 
	
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
	 	  
		return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit]) 


	def getRank(self):
       ### Make the card rank lowercase so I don't have to worry about all
       ### the possibilities of capitalization
        
		theRank = str(self.rank).lower()


       ### Create a dictionary for all the possible card values and their
       ### corresponding numerical value
		switch = {
			"ace": 14,
			"king": 13,
         "queen": 12,
         "jack": 11,
         "ten": 10,
         "nine": 9,
         "eight": 8,
         "seven": 7,
         "six": 6,
         "five": 5,
         "four": 4,
         "three": 3,
         "two": 2
      }

		return switch.get(theRank, -1)

	def setRank(self, newRank):
        ### Temporary method for quicker troubleshooting to test the getRank
        ### method on all of the possibilities

		self.rank = newRank

