# Bubble Sort short array
# Author: Sebastien Luong

from random import randrange

arr=[]
bubbleArr=[]


def bubbleSort(arr):
	swapped=True
	temp=0
	while (swapped):
		swapped=False
		for i in range(0,len(arr)-1):
			if (arr[i]>arr[i+1]):
				temp=arr[i]
				arr[i]=arr[i+1]
				arr[i+1]=temp
				swapped=True
				break
	return arr

for i in range(0,10):
	arr.append(randrange(1,100))

print "Original array: ",
print arr


print "Bubble sorted array: ", 
bubbleArr=bubbleSort(arr)
print bubbleArr 


