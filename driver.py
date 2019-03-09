from card.card import Card
from player.player import Player
from command.command import Command
from board.board import Board

def main():
	players = []
	p1 = Player('player1')
	p2 = Player('player2')

	players.extend([p1,p2])

	board = Board()

	DEPTH_LEVEL = 2
	
	#set strategy
	value = input("Enter player1's strategy (dots or color)\n")
	
	while value.upper() not in ["DOTS", "COLOR"]:
		value = input("Enter player1's strategy (dots or color)\n")
	
	p1.strategy = value
	if value == 'dots':
		p2.strategy = 'color'
	else:
		p2.strategy = 'dots'

	# set if player is human or AI
	is_human = input("Is player1 human? Enter yes or no\n")
	if is_human.upper() == "YES":
		p1.is_human = True
		p2.is_human = False
	else:
		p1.is_human = False
		p2.is_human = True

	game_completed = False

	# set if want to use alpha beta or minimax
	is_alpha_beata = input("Do you want to use alpha beta?\n")
	if is_alpha_beata.upper() == "YES":
		is_alpha_beata = True
	else:
		is_alpha_beata = False

	# set if want to read commands from a file
	read_file = input("Do you want to read input from a file? Enter yes, to read from file\n")
	read_file = read_file.upper() == 'YES'
	if read_file:
		file = open('sampleCommand.txt')

	# set if want to trace the result in a file
	new_file = None
	trace_result = input("Do you want to trace the result?\n")
	trace_result = trace_result.upper() == 'YES'
	if trace_result:
		new_file_name = input("enter file name\n")
		new_file = open(new_file_name, "w")

	cmd = ''
	score = None

	# using this counter intelligently to print spaces in trace file
	counter = 0
	while not game_completed:
		# reset static variables to trace result of each iteration
		Player.EN_LEVEL_3_COUNT = 0
		Player.EN_LEVEL_2_LIST = []
		
		for player in players:
			print(str(board))
			possibleMoves = Command.returnPossibleMoves(board, player, cmd)

			if not read_file:
				if player.is_human:
					print("Player : %s's turn, please enter a valid command to place a card" % player.name)
					cmd = input("$$ ").strip().upper()
				else:
					#player is AI and we need to find appropriate command automatically for AI player
					cmd, score = player.minimax(board, DEPTH_LEVEL, cmd, players, is_alpha_beata)
					if not player.is_human:
						
						if counter != 0:
							new_file.write("\n\n")

						new_file.write("%s\n"%Player.EN_LEVEL_3_COUNT)
						new_file.write("%s"%score)
						new_file.write("\n")
						for en in Player.EN_LEVEL_2_LIST:
							new_file.write("\n%s"%en)
			else:
				# read commands from the file
				new_cmd = file.readline().strip().upper()
				if new_cmd == '':
					# end of file is reached, close the file and exit program
					file.close()
					read_file = False
					
					# continue normal flow of game by asking user to input command
					if player.is_human:
						print("Player : %s's turn, please enter a valid command to place a card" % player.name)
						cmd = input("$$ ").strip().upper()
					else:
						#player is AI and we need to find appropriate command automatically for AI player
						cmd, score = player.minimax(board, DEPTH_LEVEL, cmd, players, is_alpha_beata)
						
						# write content in the trace file
						if not player.is_human:
							if counter != 0:
								new_file.write("\n\n")

							new_file.write("%s\n"%Player.EN_LEVEL_3_COUNT)
							new_file.write("%s"%score)
							new_file.write("\n")
							for en in Player.EN_LEVEL_2_LIST:
								new_file.write("\n%s"%en)
				else:
					# need to use this new_cmd temporary variable because we need to keep track of the previous command
					# and if end of file is reached it replaces it with empty string
					cmd = new_cmd		
			
			# if command is not valid then ask user to play the command again
			if player.is_human:
				while cmd not in possibleMoves:				
					if not read_file:
						# invalid command while manually entering values, allow user to input again
						print("invalid command, try again")
						cmd = input("$$ ").strip().upper()
					else:
						# invalid command from the file, close the file and exit program
						print("invalid command %s" % cmd)
						file.close()
						exit()
			else:
				if cmd not in possibleMoves:
					# invalid command by AI, close all files and terminate program
					print("invalid command by AI player so finish the game.")
					if read_file:
						file.close()
					if new_file:
						new_file.close()
					exit()
				
			# play move
			board.play_move(cmd, player)

			# if game is finished, print winner
			if board.is_game_finished(p1, p2):
				if p1.winner and p2.winner:
					print("Player : %s won the game" % player.name)
				elif p1.winner:
					print("Player : %s won the game" % p1.name)
				else:
					print("Player : %s won the game" % p2.name)

				game_completed = True
				break
		
		# increase counter so need to print empty spaces above
		if not read_file:
			counter += 1

	# close file resources and print board in the end
	if read_file:
		file.close()
	if new_file:
		new_file.close()
	print(str(board))

main()