#!/usr/bin/python
	
import math

def isPrime(n):
	if n==1:
		return False
	elif n < 4:
		return True
	elif n % 2 == 0:
		return False
	elif n < 9:
		return True
	elif n % 3 == 0:
		return False
	else:
		r = int(math.floor(math.sqrt(n)))
		for f in range(5, r+1, 6):
			if n % f == 0:
				return False
			if n % (f+2) == 0:
				return False
	return True
			
	
def primesBelow (n):
	sum = 2
	for i in range(3, n, 2):
		if isPrime(i):
			sum += i
			print i, sum
	return sum
		
		
	
#print sum(filter(isPrime, range(2,2000)))
print primesBelow(2000000)
		
	