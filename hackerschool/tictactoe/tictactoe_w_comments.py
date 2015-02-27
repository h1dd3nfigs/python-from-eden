'''
TicTacToe Game 
1) Create the board with numbered spaces for player to pick
2) Prompt Player X to input the space number where she wants to draw X
	If her choice is valid, log what she chose in a list, and update 
	the available options for the next player
3) Do same for Player O
4) Repeat steps 2 and 3 four more times
'''

import itertools

# Map out and print the space numbers where players can draw X or O
print '''
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

# Create a function that checks if a player has tictactoe,
# If any 3 space numbers in the player's list have coordinates that 
# are all aligned, i.e. all 3 points are colinear, then it's true 
# this player wins TicTacToe
# p1, p2, p3 are each lists containing the x-, y-coordinates of 
# each point
# To see whether all 3 points are on the same line, we confirm that the slope 
# between p1 and p2 is the same as the slope between p1 and p3
# x1 and y1 are delta_x and delta_y between p1 and p2. The slope between p1 and p2 is
# y1/x1. Likewise, the slope between p1 and p3 is y2/x2. 
# If the slopes are equal, then y1/x1 = y2/x2
# or y1*x2 = x1*y2  or y1*x2 - x1*y2 = 0
# Rather than set the expression = 0, in case I end up using floats instead of int nums
# I'll just set a really low tolerance (small number like 1e-12)
# that's close to zero so I don't end up with bugs 
def colinear(trios):
	p1, p2, p3 = trios
	x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
	x2, y2 = p3[0] - p1[0], p3[1] - p1[1]
	return x2*y1 - x1*y2 < 1e-12


# Allow players to go back and forth choosing a space to draw X or O 
# five times (which means player O doesn't get to draw the last time)
for i in range(5):
	
	x_prompt = '''
	Player X, your turn. 
	Pick a space number to draw an X.\n 
	Your options are %r \n''' % options
	
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
				print 'Player X, you have TicTacToe! You win.'
				exit()
			else:
				print 'Not yet, Player X, keep Playing'
			#	pass

	o_prompt = '''
	Player O, your turn. 
	Pick a space number to draw an O.\n 
	Your options are %r \n''' % options
	
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
			'''Check if player x has tictactoe.
			If yes, stop game she wins. if no, allow player O 
			to play and then check if O won'''
			for trios in itertools.combinations(x_picks, 3):
				if colinear(trios) == True:
					print 'Player O, you have TicTacToe! You win.'
					exit()
				else:
					print 'Not yet, Player O, keep Playing'
				#	pass

print "Player X's selections: ", x_picks
print "Player O's selections: ", o_picks

'''
Compare the slopes of the 2 pairs of points to see if 3 points are colinear
OR
Check if 3 points (a,b c ) are colinear by looking at the cross-products
since in geometry, the cross-product of two vectors a and b is the area 
of the parallelogram formed by the two, when the two vectors a and b are 
aligned, then there's no space between them adn that area is equal to 0. 
So verify that a x b = 0 and b x c = 0
We can use simple cross-product function suggested by @Sven Marnach at
http://stackoverflow.com/questions/9608148/python-script-to-determine-if-x-y-coordinates-are-colinear-getting-some-e

'''
