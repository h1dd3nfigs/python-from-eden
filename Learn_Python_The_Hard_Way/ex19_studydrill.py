from sys import argv

prompt = """
Think bigger.
How many licks does it take to get to center of a tootsie pop?
"""

def dontcha():
	licks = int(raw_input(prompt))
	print "Do you really think it only takes %d licks?" % licks


script, count = argv
print "Greatist's book reporters say it takes\
%r licks to get the tootsie center" % count

dontcha()