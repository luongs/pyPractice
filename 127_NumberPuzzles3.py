#Number Puzzles III
#Program finds all three-digit Armstrong
# numbers (number whose sum of digits cubed equal to the number itself)
#Author: Sebastien Luong

for x in range(0,10):
	for y in range(0,10):
		for z in range(0,10):
			cubedSum=x**3+y**3+z**3
			digSum=x*100+y*10+z
			if(cubedSum==digSum):
				print str(x)+str(y)+str(z)
				