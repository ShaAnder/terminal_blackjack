"""
Module to define the logic
Should run after table class has been initialized
then we get terminal_paint class to paint to the screen
"""

### --- IMPORTS --- ###

# we want sleep to create a wait function, to give the user the illusion of 
# the cpu waiting to take their turn / to prevent multiple game logic actions
# triggering early
from time import sleep


# import our card class to build our cards
from card import Card

### --- VARIABLES --- ###

# we want to create our card values / suits here:
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
suit_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

# now we want to create deck based on our suits values and cards
def create_deck():
  """
  Builds our deck of cards from the Card function
  """
  deck = []
  for suit in suits:
    for card in cards:
      deck.append(Card(suit_values[suit], card, card_values[card]))
  return deck

deck = create_deck()
print(deck)