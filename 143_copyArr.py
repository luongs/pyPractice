# Creates an array with 10 random numbers and copies it to another array
# Author: Sebastien Luong
from random import randrange

arr=[]
arr2=[]
for i in range(0,10):
	arr.append(randrange(0,101))

for i in arr:
	arr2.append(i)

arr[len(arr)-1]=-7

print "Content of arr1: ",
for i in arr:
	print i, 

print

print "Content of arr2: ",
for i in arr2:
	print i,