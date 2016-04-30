#!/usr/bin/python

import sys, time

def collatz (seed, dict=None):
	series = [seed]
	while seed > 1:
		if dict != None and dict.get(seed) != None:
			series.extend(dict[seed][1:])
			break
		if seed % 2 == 0:
			seed = seed / 2
		else:
			seed = 3 * seed + 1
		series.append(seed)
	return series

#start = time.time()
#print max([collatz(x) for x in range(int(sys.argv[1]), 0, -1)], key=lambda x: len(x))
#print "took ", time.time() - start

start = time.time()
colatzDict = dict()
for i in range(1, int(sys.argv[1])):
	colatzDict[i] = collatz (i, colatzDict)
	
print max(colatzDict.values(), key=lambda x: len(x))
print "took ", time.time() - start
