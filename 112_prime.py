#!/usr/bin/env python
# determines and returns prime numbers

range1 = lambda start, end: range(start, end+1)

def isPrime(x):
	for i in range1 (2,x):
		if (i==x):
			return True
		if (x%i==0):
			return False
		
		
	

#main function
for i in range(2,21):
	
	if (isPrime(i)==True):
		print i 