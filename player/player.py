from card.card import Card

class Player:

	def __init__(self, name):
		self.name = name
		self.cards = []
		self.assign_cards()

	def assign_cards(self):
		for i in range(12):
			card = Card()
			card.set_player(self)
			self.cards.append(card)

	def get_empty_cards(self):
		cards = []
		for card in self.cards:
			if card.miniCard1.cell is None and card.miniCard2.cell is None:
				cards.append(card)

		return cards