from card.card import Card

class Player:

	def __init__(self, name):
		self.name = name
		self.cards = []
		self.assign_cards()

	def assign_cards(self):
		for i in range(12):
			card = Card()
			card.assign_player(self)
			self.cards.append(card)