#Reads data from the high score file
#Author: Sebastien Luong

print "Reading high score file..."
print "/...."
print "|...."
print "\...."
f=open("score.txt","r")
print "Your high score is: ",
print f.readline()
print "Your name is: ", 
print f.readline()
f.close()