from card.card import Card
import math
import random
from command.command import Command
from tree.node import Node

class Player:

	SAMPLE_ALPHA_BETA = [15, 8, 16, 14, 2, 4, 24, 2]
	ALPHA_BETA_COUNTER = 0

	EN_LEVEL_3_COUNT = 0
	EN_LEVEL_2_LIST = []

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

	def append_en_values(self, depth, score, node):
		# import pdb; pdb.set_trace()
		if depth == 1:
			if not (node.best[1] == math.inf or node.best[1] == -math.inf):
				del Player.EN_LEVEL_2_LIST[-1]
			Player.EN_LEVEL_2_LIST.append(score)

	def minimax(self, board, depth, cmd, players, is_alpha_beta=False, parent_node = None):
		# human is always minimizing whereas ai is always maximizing
		other_player = players[1] if self == players[0] else players[0]

		node = Node(board, cmd, parent_node, self)

		if self.is_human:
			node.best = [None, math.inf]
		else:
			node.best = [None, -math.inf]

		# import pdb; pdb.set_trace()
		if depth == 0 or board.is_game_finished(self, other_player):
			# TODO: replace this with the actual heuristic value
			score = Player.SAMPLE_ALPHA_BETA[Player.ALPHA_BETA_COUNTER]
			Player.ALPHA_BETA_COUNTER += 1
			Player.EN_LEVEL_3_COUNT += 1
			return [cmd, score]

		# use this for testing
		for move in Command.returnPossibleMoves(board, self, cmd)[0:2]:
			#print("===== %s, parent : %s =====" % (move, cmd))
		#for move in Command.returnPossibleMoves(board, self, cmd):
			# import pdb; pdb.set_trace()
			if not node.prune:
				board.play_move(move, self, node)
				next_move, score = other_player.minimax(board, depth - 1, move, players, is_alpha_beta, node)
				board.undo_move(move, node.previous_orientation)
				# import pdb; pdb.set_trace()
				
				if not node.prune:
					if is_alpha_beta:
						
						if node.parent is not None:
							parent_node_array = []
							parent_node = node.parent
							parent_node_array.append(parent_node)
							while (parent_node.best[1] == math.inf or parent_node.best[1] == -math.inf) and parent_node.parent is not None:
								parent_node = parent_node.parent
								parent_node_array.append(parent_node)

							# import pdb; pdb.set_trace()

							parent_score = parent_node.best[1]

							if parent_node.player.is_human:
								if not self.is_human and score >= parent_score:
									self.append_en_values(depth, score, node)
									# prune nodes till parent
									node.prune = True
									for prune_node in parent_node_array:
										prune_node.prune = True
										prune_node.prune_score = parent_score
								else:
									if self.is_human:
										if score < node.best[1]:
											self.append_en_values(depth, score, node)
											node.best = [move, score]
									else:
										if score > node.best[1]:
											self.append_en_values(depth, score, node)
											node.best = [move, score]
							else:
								if self.is_human and score <= parent_score:
									self.append_en_values(depth, score, node)
									# prune nodes
									node.prune = True
									for prune_node in parent_node_array:
										prune_node.prune = True
										prune_node.prune_score = parent_score
								else:
									if self.is_human:
										if score < node.best[1]:
											self.append_en_values(depth, score, node)
											node.best = [move, score]
									else:
										if score > node.best[1]:
											self.append_en_values(depth, score, node)
											node.best = [move, score]
						else:
							# root node after travering one full depth
							if self.is_human:
								if score < node.best[1]:
									self.append_en_values(depth, score, node)
									node.best = [move, score]
							else:
								if score > node.best[1]:
									self.append_en_values(depth, score, node)
									node.best = [move, score]
					else:

						if self.is_human:
							if score < node.best[1]:
								self.append_en_values(depth, score, node)
								node.best = [move, score]
						else:
							if score > node.best[1]:
								self.append_en_values(depth, score, node)
								node.best = [move, score]
				#else:
					# this node is pruned and shouldn't be evaluated
					#node.best = [None, node.prune_score]
			else:
				print("======= parent node %s and pruned move %s =====\n" % (node.move, move))
				# this node is pruned and shouldn't be evaluated
				#node.best = [None, node.prune_score]

		return node.best