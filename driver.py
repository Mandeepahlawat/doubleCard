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

	print(str(board))

	
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
			print("Player : %s's turn, please enter a valid command to place a card" % player.name)
			
			## TODO when assigninng miniCard to cell make sure to reverse the order
			## 1 will start from bottom and not from the top, also array index starts from
			## 0 but the rows starts from 1
			
			while True:	
				possibleMoves = Command.returnPossibleMoves(board, num_cards_on_board, lastCardPosition)
				print(possibleMoves)
				cmd = input("$$ ")
				if cmd not in possibleMoves:
					print("invalid command, try again")
				else:
					#check if card can be placed there, 
					# i.e. there are cards under both the positions of the card
					# place the card

					### sample commands to assign mini card to a cell
					# card = random.choice(player.get_empty_cards())
					# board.cells[0][0].set_miniCard(card.miniCard1)
					# board.cells[1][1].set_miniCard(card.miniCard1)
					# board.cells[2][2].set_miniCard(card.miniCard1)
					# board.cells[3][3].set_miniCard(card.miniCard1)
					###
					break

			if board.is_game_finished():
				print("Player : %s won the game" % player.name)
				game_completed = True
				break

		print(str(board))

main()