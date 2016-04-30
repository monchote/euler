#!/usr/bin/python

def fibonacciNumbersUpTo (upperLimit):
	values=[2]
	fib2=1
	fib1=2
	fib = fib1 + fib2;
	while fib <= upperLimit:
		if fib % 2 == 0:
			values.append(fib)
		fib2 = fib1
		fib1 = fib
		fib = fib1 + fib2
	return values
	
	
print sum(fibonacciNumbersUpTo(4000000))
		
	