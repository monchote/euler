#!/usr/bin/python
	
import math
import itertools
import time

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
			
	
def triangleNumber (n):
	return n * (n + 1) / 2
	
def primes (howMany):
	primes=[2,3]
	i = 5
	while len(primes) < howMany:
		if isPrime(i):
			primes.append(i)
		if isPrime(i+2):
			primes.append(i+2)
		i += 6
	return primes
		
def factorize (n, primes):
	factors = []
	i = 0
	while n > 1:
		if n % primes[i] == 0:
			factors.append(primes[i])
			n /= primes[i]
		else:
			i += 1
	return factors
	
def divisors (num, primes):
	factors = factorize (num, primes)
	combinations = set()
	for i in range (1, len(factors) + 1):
		combinations = combinations.union(itertools.combinations(factors, i))
	return len(combinations) + 1
	
def divisorsOptimal (num, primes):
	factors = factorize (num, primes)
	factorsSet = set(factors)
	exponents = [factors.count(x) for x in factorsSet]
	return reduce (lambda x, y: x*(y+1), exponents, 1)
	
triangles = [triangleNumber(x) for x in range(2, 40000)]
primes = primes (5000)

start = time.time()
for x in triangles:
	if divisors (x, primes) > 700:
		print x, " and it took ", time.time() - start
		break

start = time.time()
for x in triangles:
	if divisorsOptimal (x, primes) > 700:
		print x, " and it took ", time.time() - start
		break
	