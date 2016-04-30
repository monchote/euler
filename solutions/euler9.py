#!/usr/bin/python
	
def b (a):
	return (float(2000) * a - 1000**2) / (2 * a - 2000)
	
print filter(lambda x: x[1] > 0 and x[1]-int(x[1])==0, [(x, b(x)) for x in range(1, 1000)])

		
	