from card.card import Card
import math
import random
from command.command import Command

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

	def minimax(self, board, depth, cmd, players):
		# human is always minimizing whereas ai is always maximizing
		other_player = players[1] if self == players[0] else players[0]

		if self.is_human:
			best = [None, math.inf]
		else:
			best = [None, -math.inf]

		if depth == 0 or board.is_game_finished(self, other_player):
			# TODO: replace this with the actual heuristic value
			score = random.randint(1,21)
			return [cmd, score]

		# use this for testing
		#for move in Command.returnPossibleMoves(board, self, cmd)[0:2]:
		for move in Command.returnPossibleMoves(board, self, cmd):
			board.play_move(move, self)
			next_move, score = other_player.minimax(board, depth - 1, move, players)
			board.undo_move(move)

			if self.is_human:
				if score < best[1]:
					best = [move, score]
			else:
				if score > best[1]:
					best = [move, score]

		return best