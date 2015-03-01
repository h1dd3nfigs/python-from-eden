#TicTacToe Game 
import sys
import itertools

# Map out and print the space numbers where players can draw X or O
board = '''
\t TicTacToe\n
\t 7 | 8 | 9
\t -- --- --
\t 4 | 5 | 6
\t -- --- --
\t 1 | 2 | 3
'''

# Each space number is associated with an element in this list 
# Convert the list of int to str so easily compare with user inputs later
options = [str(i) for i in range(1,10)]

# Create a dict to be used as a lookup table for the x- and y-coordinates
# of a space number
board_coord = {'1':(1,1), '2': (1,2),'3': (1,3),
		'4': (2,1), '5': (2,2),'6': (2,3),
		'7': (3,1), '8': (3,2),'9': (3,3)
}

# Create empty list to keep track of Player X's and Player O's choices
x_picks = []
o_picks = []

# Create a function that checks if 3 points (p1, p2, p3) are colinear
# Compare the slope of p1 to p2 and p1 to p3 (y1/x1 and y2/x2, respectively)
# If both slopes are equal (y1/x1 = y2/x2), then the 3 points are on the same line
# Rather than compare them to zero, I cross-mulitply and assume their diff is 
# a super small number that's close to zero (1x10^-12)

# check whether a player has played 3 or more turns
# if so, check if the player has 3 colinear points
def check_winner(turn):
	global player
	print "Running check_winner function"
	if turn >= 4:
		'''Check if player x has tictactoe.
		If yes, stop game she wins. if no, allow player O 
		to play and then check if O won'''
		if player == 'X':
			picks = x_picks
		else:
			picks = o_picks

		for trios in itertools.combinations(picks, 3):
			if colinear(trios) == True:
				#print 'Player X, you have TicTacToe! You win.'
				sys.exit('Player ' + player + ', you have TicTacToe! You win.')
			else:
				print 'Not yet, Player '+ player +', keep Playing'
		
			
		if len(options) < 1:
			sys.exit('Game over! No winner.')
	else:
		return

def switch_player():
	global player
	print "Running switch_player function"
	if player == 'X':
		player = 'O'
	else:
		player = 'X'
	print player
	return

def colinear(trios):
	print "Running colinear function"
	p1, p2, p3 = trios
	x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
	x2, y2 = p3[0] - p1[0], p3[1] - p1[1]
	slopediff = x2*y1 - x1*y2
	return abs(x2*y1 - x1*y2) < 1e-12

def play():
	print "Running play function"
	global board, player
	prompt = '''
	Player %s, your turn. 
	Pick a space number to draw an %s .\n 
	%s \nYour options are %r \n''' % (player, player, board, options)
	
	pick = raw_input(prompt)

	# Check that player's selection was an available option
	# If it was not, prompt her again to choose from what's available
	while pick not in options :
		print "\tYou chose %r, but that's not a valid option.\n" % pick
		pick = raw_input(prompt)
	else:
		print "\tPlayer %s, you drew an %s in space number: %s " % (player, player, pick)

	# Log Player X's selection in her list
	if player == 'X':
		x_picks.append(board_coord[pick])
	else:
		o_picks.append(board_coord[pick])
	# Remove the selected space number from the list of available options
	
	options.remove(pick)
	
	board = "%s" % player.join(board.split(pick))
	print board
	

# Main part of program
# Allow each player a turn choose a space to draw X or O 
# five times (which means player O doesn't get to draw the last time)
player = 'X'

for turn in range(9):
	print "Turn is %s" % turn
	play()
	check_winner(turn)
	switch_player()

