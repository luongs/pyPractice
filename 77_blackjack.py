#!/usr/bin/env python
# Blackjack challenge! Python script!
# Author: Sebastien Luong

from random import randrange
from time import sleep
import os

totalPlayer=0
totalDealer=0
decision=False
dealtCard=0
randCard=0
suit=''
special=''
win=False
lose=False
ACE=1
#All face cards are considered as 10
JACK=11
QUEEN=12
KING=13
BUST=21
#Variables used to determine card value for suits
MAX_HEARTS=13
MAX_DIAMONDS=26
MAX_CLUBS=39
MAX_SPADES=52
#Array used to check if card has already been drawn
picked=False
deck=[]
for x in range(1,54): 
	deck.append(picked)

#function to clear screen
def cls():
    os.system(['clear','cls'][os.name == 'nt'])

#drawCard() randomly picks cards while avoiding repeats
def drawCard():
	while True:
		randCard=randrange(1,53)
		if (deck[randCard]==False):
			dealtCard=randCard 
			return dealtCard
		else:
			drawCard()

#nameCard() converts different card types back to 1-10 values		
def nameCard(dealtCard):
	if dealtCard<=MAX_HEARTS:
		return dealtCard
	elif MAX_HEARTS<dealtCard<=MAX_DIAMONDS:
		dealtCard=dealtCard-MAX_HEARTS
		return dealtCard
	elif MAX_DIAMONDS<dealtCard<=MAX_CLUBS:
		dealtCard=dealtCard-MAX_DIAMONDS
		return dealtCard
	else:
		dealtCard=dealtCard-MAX_CLUBS
		return dealtCard

#suitCard() returns the card's suit
def suitCard(firstCard):
	if firstCard<=MAX_HEARTS:
		suit='Heart'
		return suit
	elif MAX_HEARTS<firstCard<=MAX_DIAMONDS:
		suit='Diamonds'
		return suit
	elif MAX_DIAMONDS<firstCard<=MAX_CLUBS:
		suit='Clubs'
		return suit
	else:
		suit='Spades'
		return suit

#specialCard() identifies face cards and Aces
def specialCard(dealtCard):
	if(dealtCard==ACE):
		special='Ace'
		return special
	elif(dealtCard==JACK):
		special='Jack'
		return special
	elif(dealtCard==QUEEN):
		special='Queen'
		firstCard=10
		return special
	elif(dealtCard==KING):
		special='King'
		firstCard=10
		return special
	else:
		special=''
		return special

# main
print "You find yourself seated in a dark lit basement casino."
print "You lay down the remainder of your money and start a game of blackjack"
print 

for i in range(1):
	firstCard=drawCard()
	suit=suitCard(firstCard)
	firstCard=nameCard(firstCard)
	special=specialCard(firstCard)

	if(special==''):
		print "You get a "+str(firstCard)+" of "+suit
	elif(special =='Jack' or special=='Queen' or special=='King'): 
		print "You get a(n) "+special+ " of "+suit
		firstCard=10
	else:
		print "You get a(n) "+special+ " of "+suit
	
	secondCard=drawCard()
	suit=suitCard(secondCard)
	secondCard=nameCard(secondCard)
	special=specialCard(secondCard)
	if(special==''):
		print "You get a "+str(secondCard)+" of "+suit
	elif(special =='Jack' or special=='Queen' or special=='King'): 
		print "You get a(n) "+special+ " of "+suit
		secondCard=10
	else:
		print "You get a(n) "+special+ " of "+suit

	totalPlayer=firstCard+secondCard
	print "Your total is "+str(totalPlayer)
	print

print "Dealer's turn: "
dFirstCard=drawCard()
dFirstSuit=suitCard(dFirstCard)
dFirstCard=nameCard(dFirstCard)
dFirstSpecial=specialCard(dFirstCard)

if(dFirstSpecial==''):
	print "The dealer's first card is a "+str(dFirstCard)+" of "+dFirstSuit
elif(dFirstSpecial =='Jack' or dFirstSpecial=='Queen' or dFirstSpecial=='King'): 
	print "The dealer's first card is a(n) "+dFirstSpecial+ " of "+dFirstSuit
	dFirstCard=10
else:
	print "The dealer's first card is "+dFirstSpecial+ " of "+dFirstSuit

dSecondCard=drawCard()
dSecondSuit=suitCard(dSecondCard)
dSecondCard=nameCard(dSecondCard)
dSecondSpecial=specialCard(dSecondCard)
totalDealer=dFirstCard+dSecondCard

print "The dealer's second card is hidden. "
print 

#Decision round, hit or stay
while True:
	if(win==True):
		print "Congratulation you won and left financially and spiritually richer!!"
		break
	elif(lose==True):
		print "Sorry you lost..T___T"
		break
	else:
		print "Your total is "+str(totalPlayer)
		call='h'
		while call=='h':
			print "Hit (h), stay (s) or fold (f)?"
			call=raw_input(">")
			if call=='s':
				break
			elif call=='f':
				print "You fold"
				lose=True
			else:
				firstCard=drawCard()
				suit=suitCard(firstCard)
				firstCard=nameCard(firstCard)
				special=specialCard(firstCard)

				if(special==''):
					print "You get a "+str(firstCard)+" of "+suit
				elif(special =='Jack' or special=='Queen' or special=='King'): 
					print "You get a(n) "+special+ " of "+suit
					firstCard=10
				else:
					print "You get a(n) "+special+ " of "+suit

				totalPlayer=totalPlayer+firstCard
				if(totalPlayer>BUST):
					print "Your total is "+ str(totalPlayer)+", its over 21! Bust!"
					lose=True
					break
				else:
					print "Your total is "+str(totalPlayer)
		print
		if lose==False:
			print "The dealer shows his hand"

			if(dFirstSpecial==''):
				print "The dealer's first card is a "+str(dFirstCard)+" of "+dFirstSuit
			elif(dFirstSpecial =='Jack' or dFirstSpecial=='Queen' or dFirstSpecial=='King'): 
				print "The dealer's first card is a(n) "+dFirstSpecial+ " of "+dFirstSuit
				dFirstCard=10
			else:
				print "The dealer's first card is "+dFirstSpecial+ " of "+dFirstSuit

			if(dSecondSpecial==''):
				print "The dealer's second card is a "+str(dSecondCard)+" of "+dSecondSuit
			elif(dSecondSpecial =='Jack' or dSecondSpecial=='Queen' or dSecondSpecial=='King'): 
				print "The dealer's second card is a(n) "+dSecondSpecial+ " of "+dSecondSuit
				dSecondCard=10
			else:
				print "The dealer's second card is "+dSecondSpecial+ " of "+dSecondSuit

			print "The dealer's total is: "+ str(totalDealer)

			while (totalDealer<= 16):
				print "The dealer hits"
				dFirstCard=drawCard()
				dFirstSuit=suitCard(dFirstCard)
				dFirstCard=nameCard(dFirstCard)
				dFirstSpecial=specialCard(dFirstCard)

				if(dFirstSpecial==''):
					print "The dealer's card is a "+str(dFirstCard)+" of "+dFirstSuit
				elif(dFirstSpecial =='Jack' or dFirstSpecial=='Queen' or dFirstSpecial=='King'): 
					print "The dealer's card is a(n) "+dFirstSpecial+ " of "+dFirstSuit
					dFirstCard=10
				else:
					print "The dealer's card is "+dFirstSpecial+ " of "+dFirstSuit

				totalDealer=totalDealer+dFirstCard
				if(totalDealer>BUST):
					print "The dealer's total is "+ str(totalDealer)+", its over 21! Bust!"
					win=True
					break
				else:
					print "The dealer's total is "+str(totalDealer)
				print

			if totalDealer<totalPlayer:
				print "Your total is higher than the dealer's!"
				win=True
			if totalDealer==totalPlayer:
				print "Tie game!"
				break
# clears screen at the end of the game				
print "CLEARING SCREEN 0:)"
sleep(1.5)
cls()
