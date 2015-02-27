'''
Code CracklePop

Write a program that prints out the numbers 1 to 100 (inclusive). 
If the number is divisible by 3, printCrackle instead of the number. 
If it's divisible by 5, print Pop. 
If it's divisible by both 3 and 5, printCracklePop. 
You can use any language.

Third way: Using list comprehension
'''


# create a list of numbers 1 to 100 inclusive
nums = range(1,16)

divby3_nums = [ x % 3 for x in nums]
divby5_nums = [ x % 5 for x in nums]