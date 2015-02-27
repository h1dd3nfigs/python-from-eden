# Decide to use the sys module (with its built-in system specific features)
# Import the argv parameter or "feature" of sys, 
# allowing my script to take command line arguments
from sys import argv

# Pass the command line argument given when I run this script
# into 2 variables, named script and filename
# script is the 1st default argument of argv, aka argv[0]
# which makes sense because when you run the script, you're 
#typing 'python ex15.py other_argument' so essentially 
# the 1st string immediately following the word python or that
# python command is the script's name
# the 2nd argument passed when we run the script in command line
# will be assigned to the variable filename
script, filename = argv

# run the open function which takes a file as it's argument
# and places that argument into a file object
# Assign this newly created file object to the variable named
# 'txt'
txt = open(filename)

# output "Here's your file argument_passed_into_command_line"
print "Here's your file %r:" % filename

# Run the read() method of the file object named 'txt'
# which reads the bytes that comprise the file object
# and print or output those bytes
print txt.read()

#close the file when done with it
txt.close()

# output "Type the filename again:"
print "Type the filename again:"

# Prompt the user to make a keyboard input after the '>' that's output
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
