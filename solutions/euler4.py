#!/usr/bin/python
	
def isPalindrome (number):
	s = str(number)
	rev = s[::-1]
	return s==rev

def biggestPalindrome (digits):
	biggest = 0, 0, 0
	i = 10**digits - 1
	while i >= 10**(digits - 1):
		j = 10**digits - 1
		while j >= 10**(digits - 1):
			product = i * j
			if isPalindrome (i * j) and product > biggest[0]:
				biggest = product, i, j
		
			j -= 1
		i -= 1
	return biggest
	

print biggestPalindrome (3)
		
	