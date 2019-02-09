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

	print(str(board))



	for player in players:
		print("Player : %s turn, please enter a valid command to place a card" % player.name)
		if player.name == 'player1':
			card = random.choice(player.get_empty_cards())
			
			## TODO when assigninng miniCard to cell make sure to reverse the order
			## 1 will start from bottom and not from the top, also array index starts from
			## 0 but the rows starts from 1
			board.cells[1][1].set_miniCard(card.miniCard1)
			board.cells[1][2].set_miniCard(card.miniCard2)

		# command = input()
		# print(Command.valid(command))
		# print(command.split(' '))


	print(str(board))
	






main()