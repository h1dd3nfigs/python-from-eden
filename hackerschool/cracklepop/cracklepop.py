'''
Code CracklePop

Write a program that prints out the numbers 1 to 100 (inclusive). 
If the number is divisible by 3, printCrackle instead of the number. 
If it's divisible by 5, print Pop. 
If it's divisible by both 3 and 5, printCracklePop. 
You can use any language.

First way: using functions
'''

# create a list of numbers 1 to 100 inclusive
nums = range(1,101)


# function checks if number is divisible by 3
# if yes, returns Crackle 
def divides_by_3_and_5(num):
	status = ''
	if num % 3 == 0:
		status += 'Crackle'
		status += divides_by_5(num)
		return status
	else:
		status += divides_by_5(num)
		return status


def divides_by_5(num):
	if num % 5 == 0:
		status = 'Pop'
	else:
		status = ''
	return status 


for i in range(len(nums)):
	status = divides_by_3_and_5(nums[i])
	if status == '':
		print nums[i]
	else: 
		print status
