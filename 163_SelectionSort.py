# Sorts array using selection Sorts
# Author: Sebastien Luong

def selectionSort(arr):
	min=0
	index=0
	minIndex=0
	arrSize=len(arr)
	sortedArr=[]
	for i in arr:
		min=i
		minIndex=index
		for x in arr:
			if x<i and x<min: 
				min=x
				print min
				minIndex=index
			index+=1	
		tmp=(arr.pop(minIndex))
		sortedArr.append(tmp)
		arr[arr.index(i)]=tmp
		index=0
		print sortedArr
	return sortedArr

arr=[5,1,12,-5]
sortedArr=[]
sortedArr=selectionSort(arr)
#print sortedArr

