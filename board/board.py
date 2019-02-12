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