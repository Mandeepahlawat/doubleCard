class Command:
	VALID_CARD_HORIZONTAL_ROTATION = ['1','2','3','4','5','6','7','8']
	VALID_CARD_VERTICAL_ROTATION = ['1','2','3','4','5','6','7','8']
	VALID_BOARD_COLUMN = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	VALID_BOARD_ROW = ['1','2','3','4','5']

	CARD_ROTATION_WITH_2_POSITIONS = ['1','3','5','7']
	
	# TODO detech edge commands

	@classmethod
	def valid(cls, command_text):
		command_list = list(command_text)
		if (command_list[0] == '0'
			and command_list[1] in cls.VALID_CARD_ROTATION
			and command_list[2].upper() in cls.VALID_BOARD_COLUMN
			and command_list[3] in cls.VALID_BOARD_ROW
		):
			return True
		elif (
			command_list[0].upper() in cls.VALID_BOARD_COLUMN
			and command_list[1] in cls.VALID_BOARD_ROW
			and command_list[2].upper() in cls.VALID_BOARD_COLUMN
			and command_list[3] in cls.VALID_BOARD_ROW
			and command_list[4] in cls.VALID_CARD_ROTATION
			and command_list[5].upper() in cls.VALID_BOARD_COLUMN
			and command_list[6] in cls.VALID_BOARD_ROW
		):
			#TODO check if location is occupied by card
			return True
		return False

		