# Reads txt from the web and displays result in python
# Author: Sebastien Luong

import urllib2 #library handles url stuff

f=urllib2.urlopen("http://cs.leanderisd.org/mitchellis.txt")
print f.readline(),
print f.readline(),

f.close()