from sys import argv

script, input_file = argv

def print_all(f):
	# take the file object, f, passed in as an argument in the 
	# print_all() function and perform the read() function which
	# reads the file object and returns it as a string
	# print command then displays that returned string to terminal
	print f.read()

def rewind(f):
	# the seek() method moves the file object's position to a specified
	# location in the file. it counts position by # of bytes into 
	# the file.  seek() takes 2 arguments
	# seek(offset, from_what). from_what is by default 0, which 
	# represents the beginning byte of the file, if from_what is 1
	# you're telling the pointer to offset from it's current position
	# and if you make from_what 2, then pointer goes to end of file
	# Below we are saying, set the position to the beginning byte in
	# this file object
	# if i set offset to 22, our position is the last byte 
	# on the 1st line of the file named yum_test7.txt so printing 
	# f.readline() from that position just prints a blank space aka
	# it prints a newline character (\n)
	f.seek(2)

def print_a_line(line_count, f):
	# readline() is a file object method that reads a single line
	# from a file and leaves a newline character (\n) at the end of the string
	print line_count, f.readline()

# open() method takes the file, input_file, and assigns it to the
# variable, current_file, in the form of a file object
current_file = open(input_file)

print "First Let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

# increment current_line value by 1, so it's now 2
# one way of writing that is 
# current_line = current_line + 1
# another way is...
current_line += 1
print_a_line(current_line, current_file)

# increment current_line value by 1, so it's now 3
current_line += 1
print_a_line(current_line, current_file)
