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
	def returnPossibleMoves(cls, board, player, cmd, recycle=False):
		possibleMoves = []
		#Regular moves
		if len(player.get_empty_cards()) != 0 or recycle == True:
			for row_index, row in enumerate(Board.BOARD_ROWS):
				for col_index, col in enumerate(Board.BOARD_COLUMNS):
					cell = board.get_cell_by_string_position(col+row)
					#check if cell is empty
					if cell.miniCard == None:
						#check if the cell is not on top the empty cell
						if row == '1' or board.get_cell_by_string_position(col + board.BOARD_ROWS[row_index-1]).miniCard != None:
							#get all the neighbouring cells
							neighbours = board.getNeighbouringCells(row_index, col_index)
							for neighbour_index, neighbour in enumerate(neighbours):
								#check if the neighbour is not out of range
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

			#get the last placed or moved card on board
			values = cmd.split(" ")
			last_orientation = values[-2]
			last_position1 = values[-1]
			#last_positionY1 = values[-1:]
			if last_orientation in ['1', '3', '5', '7']:
				last_position2 = chr(ord(last_position1[0]) + 1) + last_position1[1:]
				#last_positionY2 = last_positionY1
			else:
				last_position2 = last_position1[0] + str(int(last_position1[1:]) + 1)
				#last_positionY2 = chr(ord(last_positionY1) + 1)

			#add the last card placed or moved in visited
			visited = [last_position1, last_position2]
			#iterate over board
			for row_index, row in enumerate(Board.BOARD_ROWS):
				for col_index, col in enumerate(Board.BOARD_COLUMNS):
					#if not visited
					if col+row not in visited:
						visited.append(col+row)
						cell = board.get_cell_by_string_position(col+row)

						#find the corresponding cell
						corresponding_cell = None
						corresponding_cell_orientation = None
						#if cell is not empty
						if cell.miniCard != None:
							cell_orientation = cell.miniCard.card.orientation
							neighbours = board.getNeighbouringCells(row_index, col_index)
							for neighbour_index, neighbour in enumerate(neighbours):
								#check if the neighbour is not out of range
								if neighbour != "None":
									#check if neighbour is empty
									if neighbour.miniCard != None:
										#if neighbour belongs to same card
										if cell.miniCard.card == neighbour.miniCard.card:
											if neighbour_index == 0:
												corresponding_cell = col + str(int(row) + 1)
												corresponding_cell_orientation = 'even'
											else:
												corresponding_cell = chr(ord(col) + 1) + row
												corresponding_cell_orientation = 'odd'

						top_is_clear = False
						if corresponding_cell != None:
							visited.append(corresponding_cell)
							#check if top of this card is empty
							if str(int(corresponding_cell[1:]) + 1) == '12':
								top_is_clear = True
							elif corresponding_cell_orientation == 'even':
								if (board.get_cell_by_string_position(col + str(int(row) + 2)).miniCard == None):
									top_is_clear = True
							elif corresponding_cell_orientation == 'odd':
								if ((board.get_cell_by_string_position(col + str(int(row) + 1)).miniCard == None
									and board.get_cell_by_string_position(chr(ord(col) + 1) + str(int(row) + 1)).miniCard == None)
								):
									top_is_clear = True

						if top_is_clear:
							moves = cls.returnPossibleMoves(board, player, cmd, True)

							#remove the moves that includes placing card on top of the card to be moved
							moves_copy = moves[:]
							for move in moves_copy:
								if corresponding_cell_orientation == "even":
									if move.split(" ")[-1] == col + str(int(row) + 2):
										moves.remove(move)
									if move.split(" ")[-1] == chr(ord(col) - 1) + str(int(row) + 2) and move.split(" ")[-2] in ['1','3','5','7']:
										moves.remove(move)
								if corresponding_cell_orientation == "odd":
									if (move.split(" ")[-1] == col + str(int(row) + 1)
										or move.split(" ")[-1] == chr(ord(col) + 1) + str(int(row) + 1)
									):
										moves.remove(move) 

							#change the regular returned commands to recycle commands
							for move_index, move in enumerate(moves):
									moves[move_index] = col + row + " " + corresponding_cell + move[1:]

							#add this card's change in orientations as valid commands
							if corresponding_cell_orientation == "even":
								if board.get_cell_by_string_position(chr(ord(col) + 1) + row).miniCard != None:
									moves.append(col + row + " " + corresponding_cell + " 1 " + col + row)
									moves.append(col + row + " " + corresponding_cell + " 3 " + col + row)
									moves.append(col + row + " " + corresponding_cell + " 5 " + col + row)
									moves.append(col + row + " " + corresponding_cell + " 7 " + col + row)
	
								arr = ['2','4','6','8']
								arr.remove(cell_orientation)
								for orientation in arr:
									moves.append(col + row + " " + corresponding_cell + " " + orientation + " " + col + row)

							elif corresponding_cell_orientation == "odd":
								if str(int(row) + 1) != '12':
									moves.append(col + row + " " + corresponding_cell + " 2 " + col + row)
									moves.append(col + row + " " + corresponding_cell + " 4 " + col + row)
									moves.append(col + row + " " + corresponding_cell + " 6 " + col + row)
									moves.append(col + row + " " + corresponding_cell + " 8 " + col + row)
								
								arr = ['1','3','5','7']
								arr.remove(cell_orientation)
								for orientation in arr:
									moves.append(col + row + " " + corresponding_cell + " " + orientation + " " + col + row)

							
							possibleMoves.extend(moves)

								

		return possibleMoves