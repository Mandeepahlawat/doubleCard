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

	
	#set strategy
	while(True):
		value = input("Enter player1's strategy (dots or color)\n")
		if value == 'dots':
			p1.strategy = value
			p2.value = 'color'
			break
		elif value == 'color':
			p1.strategy = value
			p2.value = 'dots'
			break

	for player in players:
		print("Player : %s's turn, please enter a valid command to place a card" % player.name)
		
		## TODO when assigninng miniCard to cell make sure to reverse the order
		## 1 will start from bottom and not from the top, also array index starts from
		## 0 but the rows starts from 1
		
		while True:	
			cmd = input("$$ ")
			if not Command.valid(cmd):
				print("invalid command")
			else:
				#check if card can be placed there, 
				# i.e. there are cards under both the positions of the card
				# place the card
				break

		#print(str(board))

main()