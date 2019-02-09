class Cell:

	def __init__(self):
		self.miniCard = None

	def set_player(self, player):
		self.player = player

	def set_miniCard(self, card):
		self.miniCard = card
		card.cell = self
		# self.miniCard.set_cell(self)

	def __str__(self):
		if self.miniCard:
			return "%s" % str(self.miniCard)
		else:
			return ""