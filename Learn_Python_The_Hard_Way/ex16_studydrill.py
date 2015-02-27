from sys import argv

script, filename = argv

poesie = open(filename)

print poesie.read()
