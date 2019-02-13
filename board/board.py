from board.cell import Cell 

class Board:

	BOARD_COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	BOARD_ROWS = ['1','2','3','4','5','6','7','8','9','10','11','12']

	def __init__(self):
		# initialize board cells as array of arrays 
		self.cells = []
		for row in reversed(Board.BOARD_ROWS):
			row = []
			for col in Board.BOARD_COLUMNS:
				row.append(Cell())
			self.cells.append(row)

	def get_cell(self, row_index, col_index):
		self.cells[row_index][col_index]
		
	def get_column(self, index):
		return [row[index] for row in self.cells]

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

	def check_consecutive_color_text(self, rows):
		import pdb; pdb.set_trace()
		for row in rows:
			if len(row) > 3:
				for r in range(len(row) - 3):
					if(row[r].text() is not None
						and row[r].text() == row[r+1].text()
						and row[r+1].text() == row[r+2].text()
						and row[r+2].text() == row[r+3].text()
					):
						# same text
						return True
					if(row[r].color() is not None
						and row[r].color() == row[r+1].color()
						and row[r+1].color() == row[r+2].color()
						and row[r+2].color() == row[r+3].color()
					):
						# same color in row
						return True

	def is_game_finished(self):
		# check for all rows
		cols, rows, fdiag, bdiag = self.get_row_column_diagonals()

		if(self.check_consecutive_color_text(cols)
			or self.check_consecutive_color_text(rows)
			or self.check_consecutive_color_text(fdiag)
			or self.check_consecutive_color_text(bdiag)
		):
			return True
		else:
			return False
		# for i in range(len(Board.BOARD_ROWS)):
		# 	row = self.cells[i]
		# 	for r in range(len(row) - 3):
		# 		print(r)
		# 		if(row[r].text() == row[r+1].text()
		# 			and row[r+1].text() == row[r+2].text()
		# 			and row[r+2].text() == row[r+3].text()
		# 		):
		# 			# same text
		# 			return True
		# 		if(row[r].color() == row[r+1].color()
		# 			and row[r+1].color() == row[r+2].color()
		# 			and row[r+2].color() == row[r+3].color()
		# 		):
		# 			# same color in row
		# 			return True
		
		# # check for all columns
		# for i in range(len(Board.BOARD_COLUMNS)):
		# 	col = self.get_column(i)
		# 	for c in range(len(col) - 3):
		# 		if(col[c].text() == col[c+1].text()
		# 			and col[c+1].text() == col[c+2].text()
		# 			and col[c+2].text() == col[c+3].text()
		# 		):
		# 			return True
		# 		if(col[c].color() == col[c+1].color()
		# 			and col[c+1].color() == col[c+2].color()
		# 			and col[c+2].color() == col[c+3].color()
		# 		):
		# 			return True

	def getNeighbouringCells(self, row_index, col_index):
		neighbours = []
		if row_index == 0 and col_index == 0:
			#neighbours.append("None")
			neighbours.append(self.get_cell(row_index+1, col_index))
			neighbours.append(self.get_cell(row_index, col_index+1))
		elif row_index == 11 and col_index == 7:
			#neighbours.append(self.get_cell(row_index, col_index-1))
			neighbours.append("None")
			neighbours.append("None")
		elif row_index == 0 and col_index == 7:
			#neighbours.append(self.get_cell(row_index, col_index-1))
			neighbours.append(self.get_cell(row_index+1, col_index))
			neighbours.append("None")
		elif row_index == 11 and col_index == 0:
			#neighbours.append("None")
			neighbours.append("None")
			neighbours.append(self.get_cell(row_index, col_index+1))
		elif row_index == 0:
			#neighbours.append(self.get_cell(row_index, col_index-1))
			neighbours.append(self.get_cell(row_index+1, col_index))
			neighbours.append(self.get_cell(row_index, col_index+1))
		elif col_index == 0:
			#neighbours.append("None")
			neighbours.append(self.get_cell(row_index+1, col_index))
			neighbours.append(self.get_cell(row_index, col_index+1))
		elif row_index == 11:
			#neighbours.append(self.get_cell(row_index, col_index-1))
			neighbours.append("None")
			neighbours.append(self.get_cell(row_index, col_index+1))
		elif col_index == 7:
			#neighbours.append(self.get_cell(row_index, col_index-1))
			neighbours.append(self.get_cell(row_index+1, col_index))
			neighbours.append("None")
		else:
			#neighbours.append(self.get_cell(row_index, col_index-1))
			neighbours.append(self.get_cell(row_index+1, col_index))
			neighbours.append(self.get_cell(row_index, col_index+1))
		
		return neighbours
		

	def __str__(self):
		# represent board in form of a matrix
		output = ""
		for row_index, row in enumerate(reversed(Board.BOARD_ROWS)):
			output += '\n'
			output += "|%2s|" % row
			for col_index, col in enumerate(Board.BOARD_COLUMNS):
				output += "|%10s|" % self.cells[row_index][col_index]

		output += '\n'
		output += '|  |'
		for col in Board.BOARD_COLUMNS:
			output += "|%10s|" % col


		return output