#One shot hi-lo game
#Author: Sebastien Luong

from random import randrange

secretNum=randrange(1,101)
print "I'm thinking of a number between 1 - 100. Try to guess it."
userNum=raw_input(">")
if (secretNum>int(userNum)):
	print "Sorry, you're too low. I was thinking of "+str(secretNum)
elif (secretNum<int(userNum)):
	print "Sorry, you're too high. I was thinking of "+str(secretNum)
else:
	print "Right you guessed it!"+str(secretNum)