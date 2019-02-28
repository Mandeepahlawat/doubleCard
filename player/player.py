from card.card import Card

class Player:

	def __init__(self, name):
		self.name = name
		self.cards = []
		self.assign_cards()
		self.winner = False
		self.is_human = True
	
	def setPlayerStrategy(self, strategy):
		self.strategy = strategy
		
	def assign_cards(self):
		for i in range(12):
			card = Card()
			card.set_player(self)
			self.cards.append(card)

	def get_empty_cards(self):
		cards = []
		for card in self.cards:
			if not card.placed_on_board:
				cards.append(card)

		return cards