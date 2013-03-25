#Grab adjective/Titles and randomly generate a movie Titles
#Author: Sebastien Luong

import urllib2
from random import randrange

adjectives=[]
nouns=[]
fAdj=urllib2.urlopen("http://cs.leanderisd.org/txt/adjectives.txt")
fNoun=urllib2.urlopen("http://cs.leanderisd.org/txt/nouns.txt")
# leaves list of adjectives into adjective array
adjectives=fAdj.read().split("\n")
nouns=fNoun.read().split("\n")

print "Creating random movie title...."
print "The "+adjectives[randrange(1,len(adjectives))]+" "+nouns[randrange(1,len(nouns))]
