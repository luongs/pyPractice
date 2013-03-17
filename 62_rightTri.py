#Right triangle checker
#Author: Sebastien Luong

num1=0
num2=0
num3=0
choice=True
hyp=0
sides=0

print 'Enter three integers: '
while choice==True:
	print 'Side 1', 
	num1=int(raw_input(' '))
	if num1>=0:
		break
	else: 
		print str(num1)+ ' is negative. Try again.'
while choice==True:
	print 'Side 2', 
	num2=int(raw_input(' '))
	if num2>=num1:
		break
	else: 
		print str(num2)+ ' is smaller than '+ str(num1)+ ' . Try again.'

while choice==True:
	print 'Side 3', 
	num3=int(raw_input(' '))
	if num3>=num2:
		break
	else: 
		print str(num3)+ ' is smaller than '+ str(num2)+ ' . Try again.'

print "Your three sides are "+str(num1)+' '+str(num2)+ ' '+str(num3)
hyp=num3**2
sides=num2**2+num1**2
if(hyp==sides):
	print "These sides do make a right triangle!!"
else: 
	print "NOT a right angle triangle!!"
