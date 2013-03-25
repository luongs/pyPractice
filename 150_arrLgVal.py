# Program creates a random array and finds the largest value and slot number
# Author: Sebastien Luong
from random import randrange

arr=[]
slot=0
max=0
maxNum=0
maxSlot=0
for i in range(0,10):
	arr.append(randrange(1,101))

for i in arr: 
	print i, 
	if i>max:
		max=i
		maxSlot=slot
	slot+=1

print "The max number in array is: "+str(max)+" and the slot number is "+str(maxSlot)
