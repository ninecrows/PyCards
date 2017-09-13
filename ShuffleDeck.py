#! /usr/bin/env python3
import random

# Cards in each suit
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Suits of cards
suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

# Start with an empty deck and fill it with on card of each type in each suit
deck = []
for card in cards:
 for suit in suits:
  deck.append(card + " of " + suit)

# Make sure we got the right number of cards in the deck
decksize = len(deck)
print (str(decksize) + " cards in a deck")

# Shuffle the cards by walking through each location and swapping it with a
# randomly chosen location in the deck.
for item in range(0, decksize):
 dest = random.randint(0, decksize - 1)
 # Swap by saving the contents of the destination spot, copying the source
 # spot there and then placing our saved card in the source location.
 temp = deck[dest]
 deck[dest] = deck[item]
 deck[item] = temp
  
print(deck);
