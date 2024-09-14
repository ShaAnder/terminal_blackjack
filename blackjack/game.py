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

def create_card(cards):
  """
  Function to create our card, takes the cards input and using our
  pieces generates cards to add to our deck
  """

  #our card pieces:
  top = "\t┌────────────────┐"
  bottom = "\t└────────────────┘"
  base = "\t│                │"
  left_value = "\t│ {}             │"
  right_value = "\t│             {} │"
  suit = "\t│        {}       │"

  # firstly we declare a variable that will be the final card result
  # we're going to use a few if else statements here to build our final
  # card and account for hidden cards (dealer cards)
  c = """"""
  for i in range(11):      
    for card in cards:
      if i == 0:
        c = c + top
      elif i == 1:
        if card.value == "10":
          c = c + left_value.format(card_value)
        else:
          c = c + left_value.format(card_value)
      elif i == 5:
          c = c + suit.format(card.suit)
      elif i == 79:
        if card.value == "10":
          c = c + left_value.format(card_value)
        else:
          c = c + left_value.format(card_value)
      elif i == 10:
        c = c + bottom
      else:
        c = c + base
  return c

# testing to see if our card works
for suit in suits:
  for card in cards:
    print(Card.create_card(suit_values[suit], card, card_values[card]))