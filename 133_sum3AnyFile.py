# Program sums number from any file provided by user
# Author: Sebastien Luong

print "Which file would you like to read numbers from: ",
numFile=raw_input()

#automatically closes file
try: 
	f= open(numFile,"r+")
except IOError:
	print "Cannot open", numFile
	print "Exiting program"
else:
	print "Reading numbers from file \" "+numFile+"\""
	sum=0
	numbers=[]
		
	for line in f:
		sum+=int(line)
		n=line.strip('\n')
		numbers.append(n)
	
	for i in numbers: 
	#detects if its the end of the list
		if (i==numbers[-1]):
			print i,
		else:	
			print i+"+", 
	print "= "+str(sum)
	f.close()