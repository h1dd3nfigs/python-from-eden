#TicTacToe Game 
import sys
import itertools

# Map out and print the space numbers where players can draw X or O
game_map = '''
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
board = {'1':(1,1), '2': (1,2),'3': (1,3),
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
def colinear(trios):
	p1, p2, p3 = trios
	x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
	x2, y2 = p3[0] - p1[0], p3[1] - p1[1]
	slopediff = x2*y1 - x1*y2
	return abs(x2*y1 - x1*y2) < 1e-12


# Allow players to go back and forth choosing a space to draw X or O 
# five times (which means player O doesn't get to draw the last time)
for i in range(5):
	
	x_prompt = '''
	Player X, your turn. 
	Pick a space number to draw an X.\n 
	%s \nYour options are %r \n''' % (game_map, options)
	
	x_pick = raw_input(x_prompt)

	# Check that player's selection was an available option
	# If it was not, prompt her again to choose from what's available
	while x_pick not in options :
		print "\tYou chose %r, but that's not a valid option.\n" % x_pick
		x_pick = raw_input(x_prompt)
	else:
		print "\tPlayer X, you drew an X in space number: %s " % x_pick

	# Log Player X's selection in her list
	x_picks.append(board[x_pick])
	# Remove the selected space number from the list of available options
	options.remove(x_pick)

	if i >= 2:
		'''Check if player x has tictactoe.
		If yes, stop game she wins. if no, allow player O 
		to play and then check if O won'''
		for trios in itertools.combinations(x_picks, 3):
			if colinear(trios) == True:
				#print 'Player X, you have TicTacToe! You win.'
				sys.exit('Player X, you have TicTacToe! You win.')
			else:
				print 'Not yet, Player X, keep Playing'
			#	pass

	if len(options)< 1:
		sys.exit('Game over! No winner.')


	o_prompt = '''
	Player O, your turn. 
	Pick a space number to draw an O.\n 
	%s \nYour options are %r \n''' % (game_map, options)
	
	o_pick = raw_input(o_prompt)

	# Check that player's selection was an available option
	# If it was not, prompt her again to choose from what's available
	while o_pick not in options:
		print "\tYou chose %r, but that's not a valid option.\n" % o_pick
		o_pick = raw_input(o_prompt)
	else:
		print "\tPlayer O, you drew an O in space number: %s " % o_pick

	# Log Player O's selection in her list
	o_picks.append(board[o_pick])

	#Remove the selected space number from the list of available options
	options.remove(o_pick)
	if i >= 2:
			'''Check if player o has tictactoe.
			If yes, stop game she wins. if no, allow player O 
			to play and then check if O won'''
			for trios in itertools.combinations(o_picks, 3):
				if colinear(trios) == True:
					sys.exit('Player O, you have TicTacToe! You win.')
				else:
					print 'Not yet, Player O, keep Playing'
				#	pass


print "Player X's selections: ", x_picks
print "Player O's selections: ", o_picks
