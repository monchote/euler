#!/usr/bin/python

import math, time

start = time.time() * 1000

def isMultipleOfAny (candidate, numbers):
	isMultiple = False;
	for n in numbers:
		isMultiple = isMultiple or (candidate % n == 0);
	return isMultiple;

multipleOf2or3 = lambda x:isMultipleOfAny(x, [3,5]);

print sum(filter(multipleOf2or3, range(1,10000000))), " and it took ", time.time() * 1000 - start

start = time.time() * 1000
def sumMutliplesOf (num, limit):
	limit = int(math.floor((limit - 1)/num))
	return num * (limit * (limit + 1) / 2)
	
print sumMutliplesOf (3, 10000000) + sumMutliplesOf (5, 10000000) - sumMutliplesOf (15, 10000000), " and it took ", time.time() * 1000 - start