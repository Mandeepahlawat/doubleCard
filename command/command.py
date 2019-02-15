from board.board import Board

class Command:
	VALID_CARD_ROTATION = ['1','2','3','4','5','6','7','8']

	SIDE_1_ROTATIONS = VALID_CARD_ROTATION[0:4]
	SIDE_2_ROTATIONS = VALID_CARD_ROTATION[4:]

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
	def returnPossibleMoves(cls, board, num_cards_on_board, lastCardPosition):
		possibleMoves = []
		#Regular moves
		if num_cards_on_board < 24:
			for row_index, row in enumerate(Board.BOARD_ROWS):
				for col_index, col in enumerate(Board.BOARD_COLUMNS):
					cell = board.get_cell_by_string_position(col+row)
					#check if cell is empty
					if(cell.miniCard == None):
						#check if the cell is not on top the empty cell
						if row == '1' or board.get_cell_by_string_position(col + board.BOARD_ROWS[row_index-1]).miniCard != None:
							#get all the neighbouring cells
							neighbours = board.getNeighbouringCells(row_index, col_index)
							for neighbour_index, neighbour in enumerate(neighbours):
								#check if the neighbour is not out of range #(condition can cause error)
								if neighbour != "None":
									#check if neighbour is empty
									if neighbour.miniCard == None:
										#check if neighbour is not hanging on empty cell
										if (row == '1'
											or neighbour_index == 0
											or (neighbour_index == 1 and board.get_cell_by_string_position(Board.BOARD_COLUMNS[col_index+1] + Board.BOARD_ROWS[row_index-1]).miniCard != None)
										):
											if neighbour_index == 0:
												possibleMoves.append("0 2 " + board.BOARD_COLUMNS[col_index]  + str(row_index+1))
												possibleMoves.append("0 4 " + board.BOARD_COLUMNS[col_index]  + str(row_index+1))
												possibleMoves.append("0 6 " + board.BOARD_COLUMNS[col_index]  + str(row_index+1))
												possibleMoves.append("0 8 " + board.BOARD_COLUMNS[col_index]  + str(row_index+1))
											if neighbour_index == 1:
												possibleMoves.append("0 1 " + board.BOARD_COLUMNS[col_index]  + str(row_index+1))
												possibleMoves.append("0 3 " + board.BOARD_COLUMNS[col_index]  + str(row_index+1))
												possibleMoves.append("0 5 " + board.BOARD_COLUMNS[col_index]  + str(row_index+1))
												possibleMoves.append("0 7 " + board.BOARD_COLUMNS[col_index]  + str(row_index+1))
		else:
			#Recycling moves											
			#TODO	
			for row_index, row in enumerate(reversed(Board.BOARD_ROWS)):
				for col_index, cell in enumerate(Board.BOARD_COLUMNS):
					cell = board.cells[row_index][col_index]
					#check if cell is not empty or its not the card just placed by the other player

					#### READ: uncomment this line when you are working as it causes program to not run
					#if(cell.miniCard != None or (board.BOARD_COLUMNS[col_index]  + str(row_index+1) != lastCardPosition)):
						#cell minicard problem how to know this card belongs to which neighbour?

		return possibleMoves	