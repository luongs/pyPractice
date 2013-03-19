#Number puzzles 2
#fun1() determines all two digits <=56 and >10
#fun2() determines two digit numbers reversed which equals 
#the sum of its digits. 
#Author Sebastien Luong
def fun1():	
	sum=0
	for i in range(10,100):
		if(i<=56):
			firstDig=i/10
			secondDig=i%10
			sumDig=firstDig+secondDig
			if(sumDig>10):
				print str(i) 	

def fun2():
	for i in range(10,100):
		firstDig=i/10
		secondDig=i%10
		sumDig=firstDig+secondDig
		reverseI=(secondDig*10)+firstDig
		diffDig=i-reverseI
		if(diffDig==sumDig):
			print str(i)

print "Number puzzles program; pick option:"
print "1) Find two digit numbers <= 56 with sums of digits >10"
print "2) Find two digits number reversed which equals the sums of its digits"
print "3) Quit"
userInput=raw_input("->")
print
if(userInput=="1"):
	fun1()
elif(userInput=="2"):
	fun2()
elif(userInput=="3"):
	print "Exiting program!"
else:
	print