# Create a variable formatter that is a string 
# composed of four string variables
formatter = "%r %r %r %r "

# Output the value of formatter which is 1 2 3 4
print formatter % (1, 2, 3, 4)

# Output the value of formatter which is 'one' 'two' 'three' 'four'
print formatter % ("one", "two", "three", "four")

# Output the value of formatter which is True False False True
print formatter % (True, False, False, True)

# Output the value of formatter which is '%r %r %r %r'
# since I guess the % symbol suggests it's looking to fill 
# the first formatter with a string????
print formatter % (formatter, formatter, formatter, formatter)

# Output the value of formatter which is 
#	I had this thing. That you could type up right.
#	But it didn't sing. So I said goodnight.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)