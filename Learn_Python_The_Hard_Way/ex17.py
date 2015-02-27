from sys import argv
from os.path import exists

#----------------------------------------
# AHHHHH!!!! MADE it work on 1 line!!!!!
#----------------------------------------

#script, from_file, to_file = argv
#print "Copying from %s to %s " % (from_file, to_file)

# we could do these two on one line, how?
# answer: by giving the open method a 2nd parameter, 'r'
#in_file = open(from_file)
#indata = open(from_file).read()

'''
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
'''

#out_file = open(to_file, 'w')
open(argv[2], 'w').write(open(argv[1]).read())
#out_file.write(in_file)

#print "Alright, all done."

# out_file.close()
#in_file.close()
