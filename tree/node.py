import math
import random

class Node:

	def __init__(self, board, move, parent, player):
		self.board = board
		self.move = move
		self.parent = parent
		self.player = player
		self.prune = False
		

	# def minimax(self, board, depth, cmd, players):
	# 	# human is always minimizing whereas ai is always maximizing
	# 	other_player = players[1] if self == players[0] else players[0]

	# 	if self.is_human:
	# 		best = [None, math.inf]
	# 	else:
	# 		best = [None, -math.inf]

	# 	if depth == 0 or board.is_game_finished(self, other_player):
	# 		# TODO: replace this with the actual heuristic value
	# 		score = random.randint(1,21)
	# 		return [cmd, score]

	# 	# use this for testing
	# 	#for move in Command.returnPossibleMoves(board, self, cmd)[0:2]:
	# 	for move in Command.returnPossibleMoves(board, self, cmd):
	# 		board.play_move(move, self)
	# 		next_move, score = other_player.minimax(board, depth - 1, move, players)
	# 		board.undo_move(move)

	# 		if self.is_human:
	# 			if score < best[1]:
	# 				best = [move, score]
	# 		else:
	# 			if score > best[1]:
	# 				best = [move, score]

	# 	return best