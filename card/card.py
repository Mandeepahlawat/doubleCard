class Card:

	def __init__(self):
		self.side1 = 'o'
		self.side2= '0'

	def assign_player(self, player):
		self.player = player

	def __str__(self):
		return [self.side1, self.side2]

	def __repr__(self):
		return "<Card side1:%s side2:%s>" % (self.side1, self.side2)