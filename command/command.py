from board.board import Board

class Command:
	VALID_CARD_ROTATION = ['1','2','3','4','5','6','7','8']

	@classmethod
	def valid(cls, command_text):
		#split the command parameters by space
		command_list = command_text.upper().strip().split(" ")

		#check is command contains only alpha numeric characters
		for element in command_list:
			if not element.isalnum():
				return False

		#if it is a regular move	
		if (command_list[0] == '0' and 
			len(command_list) == 3 and 
				(len(command_list[2]) == 2 or len(command_list[2]) == 3) and
					len(command_list[1]) <= 2 and
						command_list[1].isdigit() and
							command_list[2][0].isalpha() and
								command_list[2][1].isdigit()):

			orientation = command_list[1]
			positionX = command_list[2][0]
			positionY = command_list[2][1:]

			#check for any out of range position
			if orientation not in cls.VALID_CARD_ROTATION:
				return False
			if positionX not in Board.BOARD_COLUMNS:
				return False
			if positionY not in Board.BOARD_ROWS:
				return False

			#store integer value of the alphabet
			#positionX = Board.BOARD_COLUMNS.index(positionX)

			#check for edges
			if positionX == 'H' and \
				(orientation == '1' or orientation == '3' or orientation == '5' or orientation == '7'):
				return False
			if positionY == '12' and \
				(orientation == '2' or orientation == '4' or orientation == '6' or orientation == '8'):
				return False

			return True

		#if it is a recycling move
		elif (len(command_list) == 4 and
				(len(command_list[0]) == 2 or len(command_list[0]) == 3) and 
					(len(command_list[1]) == 2 or len(command_list[1]) == 3) and
						(len(command_list[3]) == 2 or len(command_list[3]) == 3) and
							len(command_list[2]) <= 2 and
			command_list[0][0].join(command_list[1][0]).join(command_list[3][0]).isalpha() and
				command_list[0][1].join(command_list[1][1]).join(command_list[2]).join(command_list[3][1]).isdigit()):

			orientation = command_list[2]
			positionX1 = command_list[0][0]
			positionY1 = command_list[0][1:]
			positionX2 = command_list[1][0]
			positionY2 = command_list[1][1:]
			positionX3 = command_list[3][0]
			positionY3 = command_list[3][1:]

			#check for any out of range position
			if orientation not in cls.VALID_CARD_ROTATION:
				return False
			if positionX1 not in Board.BOARD_COLUMNS \
				or positionX2 not in Board.BOARD_COLUMNS \
					or positionX3 not in Board.BOARD_COLUMNS:
				return False
			if positionY1 not in Board.BOARD_ROWS \
				or positionY2 not in Board.BOARD_ROWS \
					or positionY3 not in Board.BOARD_ROWS:
				return False

			#check for edges
			if positionX3 == 'H' and \
				(orientation == '1' or orientation == '3' or orientation == '5' or orientation == '7'):
				return False
			if positionY3 == '12' and \
				(orientation == '2' or orientation == '4' or orientation == '6' or orientation == '8'):
				return False

			return True	

		else:
			return False

	@classmethod
	def returnPossibleMoves(cls, board):
		possibleMoves = []
		for row_index, row in enumerate(reversed(board)):
			for col_index, cell in enumerate(row):
				#check if cell is empty
				if(cell.miniCard == None):
					#check if the cell is not on top the empty cell
					if(row_index != 0 and board.get_cell(row_index, col_index).miiniCard != None):
						#get all the neighbouring cells
						neighbours = board.getNeighbouringCells(row_index, col_index)
						for cell in neighbours:
							#check if the neighbour is empty
							if (cell.miniCard == None):
								#todo
								
							

		return possibleMoves							
		