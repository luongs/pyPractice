# Number Puzzle I Program; Create list of pairs of pos whose sum is 60 and difft 14
# Author: Sebastien Luong

sumTotal=0
diffTotal=0

for i in range(10,100):
	for x in range(10,100):
		sumTotal=i+x
		diffTotal=i-x
		if (sumTotal==60 and diffTotal==14):
			print "("+str(i)+","+str(x)+" )"