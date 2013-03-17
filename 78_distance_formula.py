#!/usr/bin/env python
#function used to determine the distance between two points

from math import sqrt

def distanceFnc(x2,y2,x1,y1):
	distance=0.0
	distance=sqrt((x2-x1)**2+(y2-y1)**2)
	return distance

print "The distance between (-2,1) to (1,5) => " + str(distanceFnc(1,5,-2,1))
print "The distance between (-2,-3) to (-4,4) => "+ str(distanceFnc(-4,4,-2,-3))
print "The distance between (2,-3) to (-1,-2) => "+ str(distanceFnc(-1,-2,2,-3))
print "The distance between (4,5) to (4,5) => "+ str(distanceFnc(4,5,4,5))







