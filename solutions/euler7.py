#!/usr/bin/python
	
def isPrime(n):
	i = 2
	while i < n:
		if n % i == 0:
			return False
		i+=1
	return True
	
def findNthPrime (nth):
	primesFound = 1
	lastPrime = 0
	i = 3
	while primesFound < nth:
		if isPrime(i):
			primesFound += 1
			lastPrime = i
			print "prime found: ", lastPrime, " so far: ", primesFound
		i+=2
	return lastPrime
		
	
print findNthPrime(10001)

		
	