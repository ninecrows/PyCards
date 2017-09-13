#! /usr/bin/env python3

import sys

print("Testing")
print(sys.version_info)

import sys;print("%x" % sys.maxsize, sys.maxsize > 2**32)

import sys,platform
print(platform.architecture())

cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

deck = []

for card in cards:
 for suit in suits:
  deck.append(card + " of " + suit)

decksize = len(deck)
print (str(decksize) + " cards in a deck")

for item in range(0, decksize):
 import random
 dest = random.randint(0, decksize - 1)
 temp = deck[dest]
 deck[dest] = deck[item]
 deck[item] = temp
  
print(deck);

#import time
#time.sleep(10)
