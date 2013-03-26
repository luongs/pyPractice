# Find sum of even valued terms in fib sequence
# Author: Sebastien Luong

fibSum=0
fibFirst=1
fibSecond=2
#initially add fibEvenVal since it won't be included in fibSum calc
fibEvenVal=0+fibSecond
while fibSum<4000000:	
	fibSum=fibFirst+fibSecond
	if(fibSum%2==0):
		fibEvenVal+=fibSum
	fibFirst=fibSecond
	fibSecond=fibSum

print "The sum of all even fibonacci integers is "+ str(fibEvenVal)