#Number guessing game, while loop
#Author Sebastien Luong

from random import randrange

secretN= randrange(1,11)
print "Try to guess the number between 1 and 10. "
print "Your guess",
inputN=int(raw_input('>'))
while(secretN != inputN):
	print "Incorrect. Guess again."
	print "Your guess ", 
	inputN=int(raw_input('>'))
print "That's right!"