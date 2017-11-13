from player import Player

class Comparator(object):
	def __eq__(player1, player2):
		return player1.score - player2.score
		