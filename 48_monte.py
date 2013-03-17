#Three card monte
#Author Sebastien Luong

from random import randrange

print "You are invited to play a game of \'Ball and cups\' by a street peddler."
print "He shuffles the ball underneath one of the three cups"
gridA="##"
gridAA="##"
gridB="##"
gridBB='##'
gridC="##"
gridCC="##"
secretN=randrange(1,4)


print "\t"+gridA+"\t"+gridB+'\t'+gridC
print "\t"+gridAA+"\t"+gridBB+'\t'+gridCC
print "\t1 \t2 \t3"
print "Place your guess!"
guess=raw_input('>')

if(int(guess) == secretN) and (int(guess) == 1):
	gridA="AA"
	gridAA="AA"
	print "\t"+gridA+"\t"+gridB+'\t'+gridC
	print "\t"+gridAA+"\t"+gridBB+'\t'+gridCC
	print "\t1 \t2 \t3"
	print "Correct!"
elif(int(guess) == secretN) and (int(guess) == 2):
	gridB="AA"
	gridBB="AA"
	print "\t"+gridA+"\t"+gridB+'\t'+gridC
	print "\t"+gridAA+"\t"+gridBB+'\t'+gridCC
	print "\t1 \t2 \t3"
	print "Correct!"
elif(int(guess) == secretN) and (int(guess) == 3):
	gridC="AA"
	gridCC="AA"
	print "\t"+gridA+"\t"+gridB+'\t'+gridC
	print "\t"+gridAA+"\t"+gridBB+'\t'+gridCC
	print "\t1 \t2 \t3"
	print "Correct!"
else:
	print "\t"+gridA+"\t"+gridB+'\t'+gridC
	print "\t"+gridAA+"\t"+gridBB+'\t'+gridCC
	print "\t1 \t2 \t3"
	print "Sorry, the ball wasn't underneath cup "+str(guess)+" it was underneath "+str(secretN)



