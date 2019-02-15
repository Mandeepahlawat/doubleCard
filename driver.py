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

	# print(str(p1.cards[0]))
	# print(p2.cards)
	board = Board()
	num_moves = 0
	num_cards_on_board = 0

	
	#set strategy
	while True:
		#value = input("Enter player1's strategy (dots or color)\n")
		value = 'dots'
		if value == 'dots':
			p1.strategy = value
			p2.value = 'color'
			break
		elif value == 'color':
			p1.strategy = value
			p2.value = 'dots'
			break

	game_completed = False

	while not game_completed:
		for player in players:
			print(str(board))
			print("Player : %s's turn, please enter a valid command to place a card" % player.name)
			
			## TODO when assigninng miniCard to cell make sure to reverse the order
			## 1 will start from bottom and not from the top, also array index starts from
			## 0 but the rows starts from 1
			
			while True:	
				possibleMoves = Command.returnPossibleMoves(board, num_cards_on_board, lastCardPosition=None)
				print(possibleMoves)
				cmd = input("$$ ")
				if cmd.upper() not in possibleMoves:
					print("invalid command, try again")
				else:
					cell1, cell2 = board.get_cells_by_command(cmd)
					orientation = Board.get_orientation_and_cell_position(cmd)[0]

					if cmd[0] == '0':
						card = random.choice(player.get_empty_cards())
					else:
						command_list = cmd.upper().strip().split(" ")
						prev_cell1 = board.get_cell_by_string_position(command_list[0])
						prev_cell2 = board.get_cell_by_string_position(command_list[1])

						card = prev_cell1.miniCard.card

						prev_cell1.remove_miniCard()
						prev_cell2.remove_miniCard()

					if orientation in ['1', '4', '5', '8']:
						cell1.set_miniCard(card.miniCard1(orientation))
						cell2.set_miniCard(card.miniCard2(orientation))
					else:
						cell1.set_miniCard(card.miniCard2(orientation))
						cell2.set_miniCard(card.miniCard1(orientation))

					break

			if board.is_game_finished(p1, p2):
				if p1.winner and p2.winner:
					print("Player : %s won the game" % player.name)
				elif p1.winner:
					print("Player : %s won the game" % p1.name)
				else:
					print("Player : %s won the game" % p2.name)

				game_completed = True
				break

		print(str(board))

main()