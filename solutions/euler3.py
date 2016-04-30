#!/usr/bin/python
	
def largestPrimeOf (number):
	i = 2
	while (number > 1):
		if number % i == 0:
			number = number / i
		else:
			i += 1
	return i


print largestPrimeOf (600851475143)
		
	