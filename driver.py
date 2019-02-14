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
				if cmd not in possibleMoves:
					print("invalid command, try again")
				else:
					#check if card can be placed there, 
					# i.e. there are cards under both the positions of the card
					# place the card

					### sample commands to assign mini card to a cell
					card = random.choice(player.get_empty_cards())
					cell1, cell2 = board.get_cells_by_command(cmd)

					orientation = Board.get_orientation_and_cell_position(cmd)[0]

					
					# minicard1 is always placed at cell entered by the user so we need to flip color/text based on orientation
					# if((orientation in ['1', '2', '5', '6'] and card.miniCard1.color != 'red')
					# 	or (orientation in ['3', '4', '7', '8'] and card.miniCard1.color != 'white')
					# ):
					# 	card.flip_color()

					# if((orientation in ['3', '4', '5', '6'] and card.miniCard1.text != 'O')
					# 	or (orientation in ['1', '2', '7', '8'] and card.miniCard1.text != '0')
					# ):
					# 	card.flip_text()

					### use this if we just need to rotate
					if orientation in ['1', '4', '5', '8']:
						cell1.set_miniCard(card.miniCard1(orientation))
						cell2.set_miniCard(card.miniCard2(orientation))
					else:
						cell1.set_miniCard(card.miniCard2(orientation))
						cell2.set_miniCard(card.miniCard1(orientation))

						
					### use this we it can also go down, left
					# cell1.set_miniCard(card.miniCard1(orientation))
					# cell2.set_miniCard(card.miniCard2(orientation))
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