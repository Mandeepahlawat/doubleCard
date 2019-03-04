from board.cell import Cell
import random

class Board:

	BOARD_COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	BOARD_ROWS = ['1','2','3','4','5','6','7','8','9','10','11','12']
	BOARD_ROWS_TO_INDEX = {'1': 11,'2': 10,'3': 9,'4': 8,'5': 7,'6': 6,'7': 5,'8': 4,'9': 3,'10': 2,'11': 1,'12': 0}

	def __init__(self):
		# initialize board cells as array of arrays 
		self.cells = []
		for row in reversed(Board.BOARD_ROWS):
			row = []
			for col in Board.BOARD_COLUMNS:
				row.append(Cell())
			self.cells.append(row)

	@classmethod
	def get_orientation_and_cell_position(cls, command):
		command_list = command.upper().strip().split(" ")
		if command_list[0] == '0':
			orientation = command_list[1]
			cell_position = command_list[2]
		else:
			orientation = command_list[2]
			cell_position = command_list[3]

		return (orientation, cell_position)

	def get_cell(self, row_index, col_index):
		self.cells[row_index][col_index]

	# return cell based on position like A2
	def get_cell_by_string_position(self, position):
		col_index, row_index = self.get_cell_index_by_string_position(position)
		return self.cells[row_index][col_index]

	# return cells row and col indices based on position like A2
	def get_cell_index_by_string_position(self, position):
		col_index = Board.BOARD_COLUMNS.index(position[0])
		row_index = Board.BOARD_ROWS_TO_INDEX[position[1:]]
		return (col_index, row_index)

	def get_row_column_diagonals(self):
		col_len = len(self.cells)
		row_len = len(self.cells[0])
		cols = [[] for i in range(col_len)]
		rows = [[] for i in range(row_len)]
		fdiag = [[] for i in range(col_len + row_len - 1)]
		bdiag = [[] for i in range(len(fdiag))]
		min_bdiag = -col_len + 1

		for y in range(col_len):
			for x in range(row_len):
				cols[y].append(self.cells[y][x])
				rows[x].append(self.cells[y][x])
				fdiag[x+y].append(self.cells[y][x])
				bdiag[-min_bdiag+x-y].append(self.cells[y][x])

		return (cols, rows, fdiag, bdiag)

	def check_consecutive_color_text(self, rows, player1, player2):
		# use this variable, otherwise will have to create different methods
		# to handle the case where both users are winning simultaneously
		game_finished = False

		for row in rows:
			if len(row) > 3:
				for r in range(len(row) - 3):
					if(row[r].text() is not None
						and row[r].text() == row[r+1].text()
						and row[r+1].text() == row[r+2].text()
						and row[r+2].text() == row[r+3].text()
					):
						# same text
						if player1.strategy.lower() == 'dots':
							player1.winner = True
						else:
							player2.winner = True

						game_finished = True

					if(row[r].color() is not None
						and row[r].color() == row[r+1].color()
						and row[r+1].color() == row[r+2].color()
						and row[r+2].color() == row[r+3].color()
					):
						# same color in row
						if player1.strategy.lower() == 'color':
							player1.winner = True
						else:
							player2.winner = True

						game_finished = True

					if game_finished:
						return True

	def is_game_finished(self, player1, player2):
		# check for all rows
		cols, rows, fdiag, bdiag = self.get_row_column_diagonals()

		if(self.check_consecutive_color_text(cols, player1, player2)
			or self.check_consecutive_color_text(rows, player1, player2)
			or self.check_consecutive_color_text(fdiag, player1, player2)
			or self.check_consecutive_color_text(bdiag, player1, player2)
		):
			return True
		else:
			return False


	def get_cells_by_command(self, command):
		orientation, cell_position = Board.get_orientation_and_cell_position(command)
		position1_col_index, position1_row_index = self.get_cell_index_by_string_position(cell_position)

		if orientation in ['1', '3', '5', '7']:
			position2_col_index = position1_col_index + 1
			position2_row_index = position1_row_index
		else:
			position2_col_index = position1_col_index
			position2_row_index = position1_row_index - 1

		return (self.cells[position1_row_index][position1_col_index], self.cells[position2_row_index][position2_col_index])



	def getNeighbouringCells(self, row_index, col_index):
		neighbours = []
		if row_index == 0 and col_index == 0:
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index] + Board.BOARD_ROWS[row_index+1]))
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index+1] + Board.BOARD_ROWS[row_index]))
		elif row_index == 11 and col_index == 7:
			neighbours.append("None")
			neighbours.append("None")
		elif row_index == 0 and col_index == 7:
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index] + Board.BOARD_ROWS[row_index+1]))
			neighbours.append("None")
		elif row_index == 11 and col_index == 0:
			neighbours.append("None")
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index+1] + Board.BOARD_ROWS[row_index]))
		elif row_index == 0:
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index] + Board.BOARD_ROWS[row_index+1]))
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index+1] + Board.BOARD_ROWS[row_index]))
		elif col_index == 0:
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index] + Board.BOARD_ROWS[row_index+1]))
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index+1] + Board.BOARD_ROWS[row_index]))
		elif row_index == 11:
			neighbours.append("None")
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index+1] + Board.BOARD_ROWS[row_index]))
		elif col_index == 7:
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index] + Board.BOARD_ROWS[row_index+1]))
			neighbours.append("None")
		else:
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index] + Board.BOARD_ROWS[row_index+1]))
			neighbours.append(self.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index+1] + Board.BOARD_ROWS[row_index]))
		
		return neighbours

	# play a move on board
	def play_move(self, cmd, player, node=None):
		cell1, cell2 = self.get_cells_by_command(cmd)
		orientation = Board.get_orientation_and_cell_position(cmd)[0]

		if cmd[0] == '0':
			# regular command, get a random card from player cards
			card = random.choice(player.get_empty_cards())
			if node:
				node.previous_orientation = card.orientation
		else:
			# recycling command, need to remove mini cards from cell and get card from the cell
			command_list = cmd.upper().strip().split(" ")
			prev_cell1 = self.get_cell_by_string_position(command_list[0])
			prev_cell2 = self.get_cell_by_string_position(command_list[1])

			card = prev_cell1.miniCard.card

			if node:
				node.previous_orientation = card.orientation

			prev_cell1.remove_miniCard()
			prev_cell2.remove_miniCard()

		if orientation in ['1', '4', '5', '8']:
			cell1.set_miniCard(card.miniCard1(orientation), orientation)
			cell2.set_miniCard(card.miniCard2(orientation), orientation)
		else:
			cell1.set_miniCard(card.miniCard2(orientation), orientation)
			cell2.set_miniCard(card.miniCard1(orientation), orientation)

	# undo a move, remove mini card from cells
	def undo_move(self, cmd, previous_orientation=None):
		cell1, cell2 = self.get_cells_by_command(cmd)
		card = cell1.miniCard.card
		cell1.remove_miniCard()
		cell2.remove_miniCard()
		if cmd[0] != '0':
			new_cmd = "0 %s %s" % (previous_orientation, cmd.split(' ')[0])
			self.play_move(new_cmd, card.player)
		

	def __str__(self):
		# represent board in form of a matrix
		output = ""
		for row_index, row in enumerate(reversed(Board.BOARD_ROWS)):
			output += '\n'
			output += "|%2s|" % row
			for col_index, col in enumerate(Board.BOARD_COLUMNS):
				output += "|%17s|" % self.cells[row_index][col_index]

		output += '\n'
		output += '|  |'
		for col in Board.BOARD_COLUMNS:
			output += "|%17s|" % col


		return output


	def compute_EN(self):
		whiteO = 0
		redO = 0
		white0 = 0
		red0 = 0
		for row_index, row in enumerate(Board.BOARD_ROWS):
			for col_index, col in enumerate(Board.BOARD_COLUMNS, 1):
				cell = self.get_cell_by_string_position(col+row)
				if cell.miniCard != None:
					if(cell.miniCard.color == 'white' and cell.miniCard.text == 'O'):
						whiteO+=(10*row_index) + col_index
					if(cell.miniCard.color == 'red' and cell.miniCard.text == 'O'):
						redO+=(10*row_index) + col_index
					if(cell.miniCard.color == 'white' and cell.miniCard.text == '0'):
						white0+=(10*row_index) + col_index
					if(cell.miniCard.color == 'red' and cell.miniCard.text == '0'):
						red0+=(10*row_index) + col_index

		score = whiteO + (3*white0) - (2*red0) - (1.5*redO)	
		score = round(score, 1)	
		return score


		
