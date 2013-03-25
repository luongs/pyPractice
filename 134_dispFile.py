# Program opens and displays content of file
# Author: Sebastien Luong

print "Open which file? :",
xFile=raw_input()
try:
	f=open(xFile,"r")
except IOError:
	print "Invalid file"
	print "Exiting program"
else:
	for line in f:
		print line,
