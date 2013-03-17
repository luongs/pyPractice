#Generate a list of all positive two digit numbers and displays sum of their digits
#Author: Sebastien Luong

firstDig=0
secondDig=0
sumDig=0
divisor=10

for i in range(10,100):
	print str(i)+",", 
	firstDig=i/divisor
	secondDig=i%divisor
	sumDig=firstDig+secondDig
	print str(firstDig)+"+"+str(secondDig)+"= "+ str(sumDig)
	

