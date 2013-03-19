#Program asks for high score and saves it in a score text file
#Author: Sebastien Luong
print "You got a high score!"
print "Enter your high score: "
score=raw_input(">")
print "Enter your name: " 
name=raw_input(">")

f = open("score.txt", "w,r+")
f.write(score+"\n")
f.write(name+"\n")
f.close()
