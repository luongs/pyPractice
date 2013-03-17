#Counting machine
#Author: Sebastien Luong

start=0
end=0
step=0

print 'Count from: ', 
start=int(raw_input())

print 'Count to: ', 
end=int(raw_input())

print 'Count by: ', 
step=int(raw_input())

for i in range(start,end+1,step):
	print i, 