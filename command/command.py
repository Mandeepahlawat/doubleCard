from board.board import Board
class Command:
	VALID_CARD_ROTATION = ['1','2','3','4','5','6','7','8']
	
	# TODO detech edge commands

	@classmethod
	def valid(cls, command_text):
		command_list = list(command_text)
		if (command_list[0] == '0'
			and command_list[1] in cls.VALID_CARD_ROTATION
			and command_list[2].upper() in Board.BOARD_COLUMNS
			and command_list[3] in Board.BOARD_ROWS
		):
			return True
		elif (
			command_list[0].upper() in Board.BOARD_COLUMNS
			and command_list[1] in Board.BOARD_ROWS
			and command_list[2].upper() in Board.BOARD_COLUMNS
			and command_list[3] in Board.BOARD_ROWS
			and command_list[4] in cls.VALID_CARD_ROTATION
			and command_list[5].upper() in Board.BOARD_COLUMNS
			and command_list[6] in Board.BOARD_ROWS
		):
			#TODO check if location is occupied by card
			return True
		return False

		