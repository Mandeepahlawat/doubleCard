from card.miniCard import MiniCard 

class Card:

	def __init__(self):
		self.miniCard1 = MiniCard()
		self.miniCard1.set_color('red')
		self.miniCard1.set_text('0')

		self.miniCard2 = MiniCard()
		self.miniCard2.set_color('white')
		self.miniCard2.set_text('O')

	def set_player(self, player):
		self.player = player

	def __str__(self):
		return "[%s, %s]" % (str(self.miniCard1), str(self.miniCard2))