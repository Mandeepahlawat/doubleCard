class Cell:

	def __init__(self):
		self.miniCard = None
		self.player = None

	# delegate text method to minicard
	def text(self):
		if self.miniCard:
			return self.miniCard.text
		else:
			None
	
	# delegate color method to minicard
	def color(self):
		if self.miniCard:
			return self.miniCard.color
		else:
			None

	def set_player(self, player):
		self.player = player

	def set_miniCard(self, mini_card):
		self.miniCard = mini_card
		mini_card.cell = self
		self.set_player(mini_card.card.player)
		mini_card.card.placed_on_board = True
		# self.miniCard.set_cell(self)

	def __str__(self):
		if self.miniCard:
			return "%s" % str(self.miniCard)
		else:
			return ""
