#For all operations, Python follows PEMDAS (Power Exponent Multiply Divide Add Subtract)
# outputs the phrase "I will now count chickens:"
print "I will now count my chickens: "

#Outputs the word "Hens" followed by 30/6 = 5, then 25 + 5
print "Hens", 25 + 30 / 6

#Outputs the word "Roosters," followed by 25 * 3 = 75, then 75 % 4 = 18.75
# aka 18 with remainder of 3, so modulus operator (%) just produces that remainder 3
# now 100 - 3 = 97
print "Roosters", 100 - 25 * 3.0 % 4

print "Now I will count the eggs: "

# Following PEMDAS 
# 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# the 4 % 2 yields 2 with a remainder of 0, so the modulus produces 0
# 3 + 2 + 1 - 5 +   0    - 1 / 4 + 6
# then 1/4 yields 0.25 but since this division operator is happening with integers
# we drop everything after the decimal sign, so this division produces 0
# 3 + 2 + 1 - 5 +   0    -   0   + 6
# Now our adding and subtracting leaves us with 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7 ?"

# Program treats this sequence as a boolean and if true returns true else returns false
# Since 5 is NOT less than -2, it returns "False"
print 3 + 2 < 5 - 7

#outputs the phrase than performs 3+2 operation and outputs 5
print "What is 3 + 2 ? ", 3 + 2
print "What is 5 - 7 ? ", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2