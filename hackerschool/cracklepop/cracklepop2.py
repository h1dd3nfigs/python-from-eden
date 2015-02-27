'''
Code CracklePop

Write a program that prints out the numbers 1 to 100 (inclusive). 
If the number is divisible by 3, printCrackle instead of the number. 
If it's divisible by 5, print Pop. 
If it's divisible by both 3 and 5, printCracklePop. 
You can use any language.

Second way: Using nested if statements
'''


# create a list of numbers 1 to 100 inclusive
nums = range(1,101)

#iterate over each element in nums 
for i in range(len(nums)):
	# if element is divisible by both 3 and 5, print CracklePop
	if (nums[i] % 3 + nums[i] % 5) == 0 :
		print 'CracklePop'
	# if element is divisible by only 3, print Crackle
	elif nums[i] % 3 == 0:
		print 'Crackle'
	# if element is divisible by only 5, print Pop
	# use % or convert num to str then check if ends in 5 or 0
	elif nums[i] % 5 == 0: 
		print 'Pop'
	# if divisible by neither, just print the number itself
	else:
		print nums[i] 
	

