# Reads 3 numbers from file, displays and adds them 
# Author: Sebastien Luong

print "Reading numbers from file..."
f=open("3nums.txt","r")
num1=f.readline()
num2=f.readline()
num3=f.readline()
total=int(num1)+int(num2)+int(num3)

print "The three numbers are "+num1+num2+num3
print "Their totals are "+str(total)