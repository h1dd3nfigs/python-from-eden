#TicTacToe Game 
import sys
import itertools 

# Draw a game board with space numbers where players will place X or O
board = '''
\t Tic Tac Toe\n
\t 7 | 8 | 9
\t -- --- --
\t 4 | 5 | 6
\t -- --- --
\t 1 | 2 | 3
'''

# Each space number is associated with an element in this options list 
# Convert the list of int to str to easily compare with user inputs later
options = [str(i) for i in range(1,10)]

# Create a dict to be used as a lookup table for the x- and y-coordinates
# of each space number on the game board
board_coord = {'1':(1,1), '2': (1,2),'3': (1,3),
		'4': (2,1), '5': (2,2),'6': (2,3),
		'7': (3,1), '8': (3,2),'9': (3,3)
}

# Create empty lists to keep track of Player X's and Player O's choices
x_picks = []
o_picks = []

# Check whether a player has played 3 or more turns
# if so, check if her selection of 3+ spaces correspond to a combination of 
# 3 points that are colinear
def check_winner(turn, player, board):
	#print "Running check_winner function for player %s" % player
	if turn >= 4:
		if player == 'X':
			picks = x_picks
		else:
			picks = o_picks

		for trios in itertools.combinations(picks, 3):
			if colinear(trios) == True:
				sys.exit('\n***** Player ' + player + 
					', you have TicTacToe! You win. *****\n'+ board)
			#else:
			#	print 'Not yet, Player '+ player +', keep Playing'	
		
		# If all spaces on the game board are filled with Xs and Os 
		# and neither player had any colinear combos of 3 points, game's over	
		if len(options) < 1:
			sys.exit('Game over and it\'s a tie. Let\'s play again!')
	else:
		return

def switch_player(player):
	#print "Running switch_player function"
	if player == 'X':
		player = 'O'
	else:
		player = 'X'
	return player
	#print player

# Create a function that checks if 3 points (p1, p2, p3) are colinear
# Compare the slope of p1 to p2 and p1 to p3 (y1/x1 and y2/x2, respectively)
# If both slopes are equal (y1/x1 = y2/x2), then the 3 points are on the same line
# Rather than compare them to zero, I cross-mulitply and assume their diff is 
# a super small number that's close to zero (1x10^-12)
def colinear(trios):
	#print "Running colinear function"
	p1, p2, p3 = trios
	x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
	x2, y2 = p3[0] - p1[0], p3[1] - p1[1]
	return abs(x2*y1 - x1*y2) < 1e-12

def play(player, board):
	#print "Running play function"
	prompt = '''
	Player %s, it's your turn. 
	Type the space number where you'd like to draw an %s .\n 
	%s \n\t >> ''' % (player, player, board)
	# print '''%s \nYour options are %r \n''' % (board, options)
	
	pick = raw_input(prompt)

	# Check that player's selection was an available option
	# If it was not, prompt her again to choose from what's available
	while pick not in options :
		print "\tYou chose %r, but that's not a valid option.\n" % pick
		pick = raw_input(prompt)
	#else:
	#	print "\tPlayer %s, you drew an %s in space number: %s " % (player, player, pick)

	# Log the player's selection in her list of space numbers chosen to draw X or O
	if player == 'X':
		x_picks.append(board_coord[pick])
	else:
		o_picks.append(board_coord[pick])
	
	
	# As players pick a space number for placing their Xs or Os, 
	# remove that space number from this list of available options
	options.remove(pick)
	
	# Draw the X or O on the space number chosen by the player
	board = "%s" % player.join(board.split(pick))
	#print board
	return board

intro = '''
\tWelcome to Tic Tac Toe!\n
\tThe goal of the game is to get three in a row. 
\tThe first player is known as X and the second is O. 
\tPlayers alternate placing Xs and Os on the game board (below) 
\tuntil either opponent has 3 in a row or all 9 squares are filled.
\tReady.\tSet.\tLet's play!'''

print intro
player = 'X'

# Main part of program
for turn in range(9):
	#print "Turn is %s and player is %s" % (turn, player)
	board = play(player, board)
	check_winner(turn, player, board)
	player = switch_player(player)

