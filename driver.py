from card.card import Card
from player.player import Player

def main():
	players = []
	p1 = Player('player1')
	p2 = Player('player2')

	players.extend([p1,p2])

	# print(p1.cards)
	# print(p2.cards)

	for player in players:
		print("Player : %s turn, please enter a valid command to place a card" % player.name)
		command = input()
		# print(command.split(' '))

	






main()