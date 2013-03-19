#Number Puzzles IV: A New Hope
#Find the four numbers which are true for following statements
# a+b+c+d = 45
# a+2 = b-2 = c*2 = d/2
#Author: Sebastien Luong

NUMBER_SUM=45
numSum=0
for w in range(1,42):
	for x in range(1,42):
		a=w+x
		for y in range(1,42):
			b=a+y
			for z in range(1,42):
				c=b+z
				if(c==NUMBER_SUM) and (w+2==x-2) and (w+2==y*2) and (w+2==z/2):
					print str(w)+" "+str(x)+" "+str(y)+" "+str(z) 
				else: 
					c=y-z