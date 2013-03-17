#Multiplication table program
#Author: Sebastien Luong

for i in range (0,13):
	if (i==0):
		print "x |",
	elif (i==1):
		print "==+=================================================================="
		print str(i)+" |",
	else: 
		print str(i)+" |", 
	for x in range (1,10):
		if (i==0):
			print str(x)+"\t",
		else:
			print str(x*i)+"\t",
	print


