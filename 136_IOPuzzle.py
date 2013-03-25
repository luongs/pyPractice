#Opens a file and reads only every third character from the file
#Outputs results to 136_puzzle.txt
#Author: Sebastien Luong

print "Open which file? : ", 
#Add raw_input here

f=open("puzzle.txt","r")
for line in f:
	print line
f.close()