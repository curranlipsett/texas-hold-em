from Card import Card

x = Card("Five", "Hearts")
y = Card("Ace", "Hearts")

if x.getRank() > y.getRank():
	print("True")
elif x.getRank() < y.getRank():
	print("False")
else:
	print("Equal")

x.setRank("Six")
y.setRank("Six")

if x.getRank() > y.getRank():
   print("True")
elif x.getRank() < y.getRank():
   print("False")
else:
	print("Equal")
