numbers = []


def funkyFunction(i, cap):
	while i < cap:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d " % i 

print "The numbers: "

funkyFunction(10,3)

for num in numbers:
	print num