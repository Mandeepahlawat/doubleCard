from card.card import Card
from player.player import Player
from command.command import Command
from board.board import Board
import random

def main():
	players = []
	p1 = Player('player1')
	p2 = Player('player2')

	players.extend([p1,p2])

	board = Board()
	
	#set strategy
	while True:
		value = input("Enter player1's strategy (dots or color)\n")
		is_human = input("Is player1 human? Enter yes or no\n")
		if value == 'dots':
			p1.strategy = value
			p2.value = 'color'
			if is_human.upper() == "YES":
				p1.is_human = True
				p2.is_human = False
			else:
				p1.is_human = False
				p2.is_human = True
			break
		elif value == 'color':
			p1.strategy = value
			p2.value = 'dots'
			if is_human.upper() == "YES":
				p1.is_human = True
				p2.is_human = False
			else:
				p1.is_human = False
				p2.is_human = True
			break

	game_completed = False

	print("Do you want to read input from a file? Enter yes, to read from file")
	read_file = input()
	read_file = read_file.upper() == 'YES'
	if read_file:
		file = open('sampleCommand.txt')

	cmd = ''
	while not game_completed:
		for player in players:
			print(str(board))
			possibleMoves = Command.returnPossibleMoves(board, player, cmd)
			# print(possibleMoves)

			if not read_file:
				if player.is_human:
					print("Player : %s's turn, please enter a valid command to place a card" % player.name)
					cmd = input("$$ ").strip().upper()
				else:
					#player is AI and we need to find appropriate command automatically for AI player

					## TODO: replace this with value using minimax
					cmd = random.choice(possibleMoves)
			else:
				cmd = file.readline().strip().upper()
				if cmd == '':
					# end of file is reached, close the file and exit program
					file.close()
					read_file = False
					if player.is_human:
						print("Player : %s's turn, please enter a valid command to place a card" % player.name)
						cmd = input("$$ ").strip().upper()
					else:
						#player is AI and we need to find appropriate command automatically for AI player

						## TODO: replace this with value using minimax
						cmd = random.choice(possibleMoves)
						
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
				
			cell1, cell2 = board.get_cells_by_command(cmd)
			orientation = Board.get_orientation_and_cell_position(cmd)[0]

			if cmd[0] == '0':
				# regular command, get a random card from player cards
				card = random.choice(player.get_empty_cards())
			else:
				# recycling command, need to remove mini cards from cell and get card from the cell
				command_list = cmd.upper().strip().split(" ")
				prev_cell1 = board.get_cell_by_string_position(command_list[0])
				prev_cell2 = board.get_cell_by_string_position(command_list[1])

				card = prev_cell1.miniCard.card

				prev_cell1.remove_miniCard()
				prev_cell2.remove_miniCard()

			if orientation in ['1', '4', '5', '8']:
				cell1.set_miniCard(card.miniCard1(orientation), orientation)
				cell2.set_miniCard(card.miniCard2(orientation), orientation)
			else:
				cell1.set_miniCard(card.miniCard2(orientation), orientation)
				cell2.set_miniCard(card.miniCard1(orientation), orientation)

			if board.is_game_finished(p1, p2):
				if p1.winner and p2.winner:
					print("Player : %s won the game" % player.name)
				elif p1.winner:
					print("Player : %s won the game" % p1.name)
				else:
					print("Player : %s won the game" % p2.name)

				game_completed = True
				break

	if read_file:
		file.close()
	print(str(board))

main()